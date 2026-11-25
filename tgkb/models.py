"""TG Knowledge Base - core data models."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Message:
    id: int
    chat_id: int
    chat_title: str
    sender_id: Optional[int]
    sender_name: Optional[str]
    text: str
    date: datetime
    reply_to: Optional[int] = None
    media_type: Optional[str] = None
    tags: list[str] = field(default_factory=list)
    embedding: Optional[list[float]] = None

    @property
    def url(self) -> str:
        return f"https://t.me/c/{abs(self.chat_id)}/{self.id}"
