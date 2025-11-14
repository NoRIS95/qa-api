"""Pydantic схемы для ответов."""

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class AnswerBase(BaseModel):
    """Базовая схема ответа."""

    text: str


class AnswerCreate(AnswerBase):
    """Схема создания ответа."""

    text: str
    user_id: UUID


class AnswerUpdate(AnswerBase):
    """Схема обновления ответа."""

    pass


class Answer(AnswerBase):
    """Схема ответа."""

    id: int
    user_id: UUID
    question_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
