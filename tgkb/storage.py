"""Storage layer: SQLite + FTS5."""
from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Iterable, Optional

from .models import Message


SCHEMA = """
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER,
    chat_id INTEGER NOT NULL,
    chat_title TEXT,
    sender_id INTEGER,
    sender_name TEXT,
    text TEXT NOT NULL,
    date TEXT NOT NULL,
    reply_to INTEGER,
    media_type TEXT,
    tags TEXT DEFAULT '',
    PRIMARY KEY (chat_id, id)
);
CREATE VIRTUAL TABLE IF NOT EXISTS messages_fts USING fts5(
    text, chat_title, sender_name, tags,
    content='messages', content_rowid='rowid'
);
CREATE TRIGGER IF NOT EXISTS messages_ai AFTER INSERT ON messages BEGIN
    INSERT INTO messages_fts(rowid, text, chat_title, sender_name, tags)
    VALUES (new.rowid, new.text, new.chat_title, new.sender_name, new.tags);
END;
CREATE TRIGGER IF NOT EXISTS messages_ad AFTER DELETE ON messages BEGIN
    INSERT INTO messages_fts(messages_fts, rowid, text, chat_title, sender_name, tags)
    VALUES ('delete', old.rowid, old.text, old.chat_title, old.sender_name, old.tags);
END;
CREATE INDEX IF NOT EXISTS idx_messages_date ON messages(date);
CREATE INDEX IF NOT EXISTS idx_messages_chat ON messages(chat_id);
"""


class Storage:
    def __init__(self, db_path: str = "./data/tgkb.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(self.db_path))
        self.conn.row_factory = sqlite3.Row
        self.conn.executescript(SCHEMA)
        self.conn.commit()

    def upsert(self, msg: Message) -> None:
        self.conn.execute(
            """INSERT OR REPLACE INTO messages
               (id, chat_id, chat_title, sender_id, sender_name, text, date, reply_to, media_type, tags)
               VALUES (?,?,?,?,?,?,?,?,?,?)""",
            (msg.id, msg.chat_id, msg.chat_title, msg.sender_id, msg.sender_name,
             msg.text, msg.date.isoformat(), msg.reply_to, msg.media_type, ",".join(msg.tags)),
        )
        self.conn.commit()

    def upsert_many(self, msgs: Iterable[Message]) -> int:
        n = 0
        for m in msgs:
            self.upsert(m)
            n += 1
        return n

    def search(self, query: str, limit: int = 50, chat_id: Optional[int] = None):
        sql = """SELECT m.* FROM messages m
                 JOIN messages_fts f ON f.rowid = m.rowid
                 WHERE messages_fts MATCH ?"""
        params: list = [query]
        if chat_id is not None:
            sql += " AND m.chat_id = ?"
            params.append(chat_id)
        sql += " ORDER BY rank LIMIT ?"
        params.append(limit)
        cur = self.conn.execute(sql, params)
        return [dict(r) for r in cur.fetchall()]

    def stats(self):
        total = self.conn.execute("SELECT COUNT(*) FROM messages").fetchone()[0]
        chats = self.conn.execute("SELECT COUNT(DISTINCT chat_id) FROM messages").fetchone()[0]
        return {"total_messages": total, "chats": chats}

    def close(self):
        self.conn.close()
