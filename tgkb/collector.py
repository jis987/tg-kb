"""Collector: Telethon-based message importer."""
from __future__ import annotations

import asyncio
from datetime import datetime
from typing import AsyncIterator

from telethon import TelegramClient
from telethon.tl.types import Message as TGMessage

from .models import Message


async def collect(chat, limit: int = 10000, api_id: int = 0, api_hash: str = "",
                 session: str = "tgkb") -> AsyncIterator[Message]:
    client = TelegramClient(session, api_id, api_hash)
    await client.start()
    entity = await client.get_entity(chat)
    title = getattr(entity, "title", None) or getattr(entity, "username", chat)
    chat_id = entity.id
    count = 0
    async for m in client.iter_messages(entity, limit=limit):
        if not m.text:
            continue
        sender = await m.get_sender()
        name = None
        if sender:
            name = getattr(sender, "first_name", None) or getattr(sender, "title", None)
        yield Message(
            id=m.id,
            chat_id=chat_id,
            chat_title=title,
            sender_id=getattr(sender, "id", None),
            sender_name=name,
            text=m.text,
            date=m.date or datetime.utcnow(),
            reply_to=m.reply_to_msg_id,
            media_type=m.media.__class__.__name__ if m.media else None,
        )
        count += 1
        if count >= limit:
            break
    await client.disconnect()
