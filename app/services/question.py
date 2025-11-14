"""Сервис для CRUD-операций, связанных с вопросами."""

from typing import Any

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.logger import logger
from app.models.common import Question
from app.schemas.question import QuestionCreate


class QuestionService:
    """Сервис вопроса."""

    @staticmethod
    def get_all_questions(db: Session) -> list[Any]:
        """Загружает все вопросы из базы данных."""
        logger.info("Получение всех вопросов")
        return db.query(Question).all()

    @staticmethod
    def create_question(db: Session, question: QuestionCreate) -> Question:
        """Создает вопрос."""
        logger.info("Создание вопроса")
        try:
            db_question = Question(text=question.text)
            db.add(db_question)
            db.commit()
            db.refresh(db_question)
            logger.success(f"Вопрос создан! Ему присвоен id {db_question.id}")
            return db_question
        except IntegrityError as e:
            logger.error(f"Ошибка целостности при создании вопроса: {str(e)}")
            db.rollback()
            raise HTTPException(status_code=400, detail=str(e)) from e

    @staticmethod
    def get_question(db: Session, question_id: int) -> Question:
        """Загружает вопрос."""
        logger.debug(f"Получение вопроса {question_id}")
        question = db.query(Question).filter(Question.id == question_id).first()
        if not question:
            logger.warning(f"Вопрос {question_id} не найден")
            raise HTTPException(status_code=404, detail="Вопрос не найден!")
        logger.debug(f"Вопрос {question_id} получен")
        return question

    @staticmethod
    def delete_question(db: Session, question_id: int) -> Question:
        """Удаляет вопрос."""
        logger.info(f"Удаление вопроса {question_id}")
        db_question = QuestionService.get_question(db, question_id)
        db.delete(db_question)
        db.commit()
        logger.warning(f"Вопрос {question_id} удалён")
        return db_question
