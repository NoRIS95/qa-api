"""Сервис для CRUD-операций, связанных с ответами."""

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.common import Answer, Question
from app.schemas.answer import AnswerCreate


class AnswerService:
    """Сервис ответа."""

    @staticmethod
    def load_answer_from_db(answer: Answer) -> Answer:
        """Загружает ответ из базы данных."""
        return answer

    @staticmethod
    def load_answer_from_create(answer: Answer) -> Answer:
        """
        Преобразует или подготавливает объект \

        Answer после создания из входных данных.
        """
        return answer

    @staticmethod
    def create_answer(db: Session, answer: AnswerCreate, question_id: int) -> Answer:
        """Создает ответ."""
        try:
            if not db.query(Question).filter_by(id=question_id).first():
                        raise HTTPException(status_code=404,
                            detail="Не удалось ответить. Вопроса не существует!")
            db_answer = Answer(text=answer.text,
                                 user_id=answer.user_id,
                                 question_id=question_id)
            db.add(db_answer)
            db.commit()
            db.refresh(db_answer)
            db_answer = AnswerService.load_answer_from_db(db_answer)
            return db_answer
        except IntegrityError as e:
            db.rollback()
            raise HTTPException(status_code=400, detail=str(e)) from e

    @staticmethod
    def get_answer(db: Session, answer_id: int) -> Answer:
        """Загружает ответ."""
        answer = db.query(Answer).filter(Answer.id == answer_id).first()
        if not answer:
            raise HTTPException(status_code=404, detail="Ответ не найден!")
        answer = AnswerService.load_answer_from_create(answer)
        return answer

    @staticmethod
    def delete_answer(db: Session, answer_id: int) -> Answer:
        """Удаляет ответ."""
        db_answer = AnswerService.get_answer(db, answer_id)
        db.delete(db_answer)
        db.commit()
        return db_answer
