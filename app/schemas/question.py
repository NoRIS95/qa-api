"""Pydantic схемы для вопросов."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.schemas.answer import AnswerCreate


class QuestionBase(BaseModel):
    """Базовая схема вопроса."""

    text: str


class QuestionCreate(QuestionBase):
    """Схема создания вопроса."""

    text: str


class QuestionUpdate(QuestionBase):
    """Схема обновления вопроса."""

    pass


class Question(QuestionBase):
    """Схема вопроса."""

    id: int
    created_at: datetime
    answers: list[AnswerCreate] | None

    model_config = ConfigDict(from_attributes=True)
