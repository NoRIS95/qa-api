"""Сервис для CRUD-операций, связанных с вопросами."""


from typing import Any

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.common import Question
from app.schemas.question import QuestionCreate, QuestionUpdate


class QuestionService:
    """Сервис вопроса."""

    @staticmethod
    def load_question_from_db(question: Question) -> Question:
        """Загружает вопрос из базы данных."""
        return question

    @staticmethod
    def get_all_questions(db: Session) -> list[Any]:
        """Загружает все вопросы из базы данных."""
        return db.query(Question).all()

    @staticmethod
    def load_question_from_create(question: Question) -> Question:
        """
        Преобразует или подготавливает объект \

        Question после создания из входных данных.
        """
        return question

    @staticmethod
    def create_question(db: Session, question: QuestionCreate) -> Question:
        """Создает вопрос."""
        try:
            question = QuestionService.load_question_from_create(question)
            question_data = question.model_dump()
            db_question = Question(**question_data)
            db.add(db_question)
            db.commit()
            db.refresh(db_question)
            db_question =  QuestionService.load_question_from_db(db_question)
            return db_question
        except IntegrityError as e:
            db.rollback()
            raise HTTPException(status_code=400, detail=str(e)) from e

    @staticmethod
    def get_question(db: Session, question_id: int) -> Question:
        """Загружает вопрос."""
        question = db.query(Question).filter(Question.id == question_id).first()
        if not question:
            raise HTTPException(status_code=404, detail="Вопрос не найден!")
        question = QuestionService.load_question_from_create(question)
        return question

    @staticmethod
    def update_question(db: Session, question_id: int, question: QuestionUpdate)\
          -> Question:
        """Обновляет вопрос."""
        db_question = QuestionService.get_question(db, question_id)
        question_data = QuestionService.load_question_from_create(question)
        question_data = question.model_dump(exclude_unset=True)
        for key, value in question_data.items():
            setattr(db_question, key, value)
        try:
            db.commit()
            db.refresh(db_question)
            db_question = QuestionService.load_question_from_db(db_question)
            return db_question
        except IntegrityError as err:
            db.rollback()
            raise HTTPException(status_code=400,
                                detail="Неверный запрос для редактирования вопроса.")\
                                      from err

    @staticmethod
    def delete_question(db: Session, question_id: int) -> Question:
        """Удаляет вопрос."""
        db_question = QuestionService.get_question(db, question_id)
        db.delete(db_question)
        db.commit()
        return db_question
