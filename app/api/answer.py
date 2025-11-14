"""Эндпоинты для ответов."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.logger import logger
from app.schemas.answer import Answer, AnswerCreate
from app.services.answer import AnswerService

router = APIRouter()


@router.post("/questions/{question_id}/answers/", response_model=Answer)
def create_answer(
    answer: AnswerCreate, question_id: int, db: Session = Depends(get_db)
) -> Answer:
    """Роутер создания ответа."""
    logger.info(f"Создание ответа для вопроса {question_id}")
    return AnswerService.create_answer(db, answer, question_id)


@router.get("/answers/{answer_id}", response_model=Answer)
def get_answer(answer_id: int, db: Session = Depends(get_db)) -> Answer:
    """Роутер отображения конкретного ответа."""
    logger.debug(f"Получение ответа {answer_id}")
    db_answer = AnswerService.get_answer(db, answer_id)
    return db_answer


@router.delete("/answers/{answer_id}", response_model=Answer)
def delete_answer(answer_id: int, db: Session = Depends(get_db)) -> Answer:
    """Роутер удаления ответа."""
    logger.info(f"Удаление ответа {answer_id}")
    db_answer = AnswerService.delete_answer(db, answer_id)
    return db_answer
