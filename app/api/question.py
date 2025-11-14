"""Эндпоинты для вопросов."""

from collections.abc import Generator
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.question import Question, QuestionCreate
from app.services.question import QuestionService

router = APIRouter()


@router.post("/", response_model=Question)
def create_question(
    question: QuestionCreate, db: Session = Depends(get_db)
) -> Generator[Any, Any, Any]:
    """Роутер создания вопроса."""
    return QuestionService.create_question(db, question)


@router.get("/", response_model=list[Question])
def get_all_questions(db: Session = Depends(get_db)) -> Generator[Any, Any, Any]:
    """Роутер отображения всех вопросов."""
    return QuestionService.get_all_questions(db)


@router.get("/{id}", response_model=Question)
def get_question(
    question_id: int, db: Session = Depends(get_db)
) -> Generator[Any, Any, Any]:
    """Роутер отображения конкретного вопроса."""
    db_question = QuestionService.get_question(db, question_id)
    if db_question is None:
        raise HTTPException(status_code=404, detail="Вопрос не найден!")
    return db_question


@router.delete("/{id}", response_model=Question)
def delete_question(
    question_id: int, db: Session = Depends(get_db)
) -> Generator[Any, Any, Any]:
    """Роутер удаления вопроса."""
    db_question = QuestionService.delete_question(db, question_id)
    if db_question is None:
        raise HTTPException(status_code=404, detail="Вопрос не найден!")
    return db_question
