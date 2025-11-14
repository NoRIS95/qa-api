"""Эндпоинты для ответов."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.answer import Answer, AnswerCreate
from app.services.answer import AnswerService

router = APIRouter()


@router.post("/questions/{question_id}/answers/", response_model=Answer)
def create_answer(
    answer: AnswerCreate, question_id: int, db: Session = Depends(get_db)
) -> Answer:
    """Роутер создания ответа."""
    return AnswerService.create_answer(db, answer, question_id)


@router.get("/answers/{id}", response_model=Answer)
def get_answer(answer_id: int, db: Session = Depends(get_db)) -> Answer:
    """Роутер отображения конкретного ответа."""
    db_answer = AnswerService.get_answer(db, answer_id)
    if db_answer is None:
        raise HTTPException(status_code=404, detail="Ответ не найден!")
    return db_answer


@router.delete("/answers/{id}", response_model=Answer)
def delete_answer(answer_id: int, db: Session = Depends(get_db)) -> Answer:
    """Роутер удаления вопроса."""
    db_answer = AnswerService.delete_answer(db, answer_id)
    if db_answer is None:
        raise HTTPException(status_code=404, detail="Ответ не найден!")
    return db_answer
