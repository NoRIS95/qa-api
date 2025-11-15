"""Сервис для CRUD-операций, связанных с ответами."""

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.logger import logger
from app.models.common import Answer, Question
from app.schemas.answer import AnswerCreate


class AnswerService:
    """Сервис ответа."""

    @staticmethod
    def create_answer(db: Session, answer: AnswerCreate, question_id: int) -> Answer:
        """Создает ответ."""
        logger.info(
            f"Создание ответа для вопроса {question_id},\
                     пользователь: {answer.user_id}"
        )
        try:
            if not db.query(Question).filter_by(id=question_id).first():
                logger.warning(f"Вопрос {question_id} не найден при создании ответа")
                raise HTTPException(
                    status_code=404,
                    detail="Не удалось ответить. Вопроса не существует!",
                )
            db_answer = Answer(
                text=answer.text, user_id=answer.user_id, question_id=question_id
            )
            db.add(db_answer)
            db.commit()
            db.refresh(db_answer)
            logger.success(f"Ответ {db_answer.id} создан для вопроса {question_id}")
            return db_answer
        except IntegrityError as e:
            logger.error(f"Ошибка целостности при создании ответа: {str(e)}")
            db.rollback()
            raise HTTPException(status_code=400, detail=str(e)) from e

    @staticmethod
    def get_answer(db: Session, answer_id: int) -> Answer:
        """Загружает ответ."""
        logger.debug(f"Получение ответа {answer_id}")
        answer = db.query(Answer).filter(Answer.id == answer_id).first()
        if not answer:
            logger.warning(f"Ответ {answer_id} не найден")
            raise HTTPException(status_code=404, detail="Ответ не найден!")
        logger.debug(f"Ответ {answer_id} получен успешно")
        return answer

    @staticmethod
    def delete_answer(db: Session, answer_id: int) -> Answer:
        """Удаляет ответ."""
        logger.info(f"Удаление ответа {answer_id}")
        db_answer = AnswerService.get_answer(db, answer_id)
        db.delete(db_answer)
        db.commit()
        logger.warning(f"Ответ {answer_id} удалён")
        return db_answer
