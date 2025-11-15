"""Юнит-тесты для эндпоинта получения вопроса."""

from unittest.mock import Mock, patch

from fastapi import HTTPException
from fastapi.testclient import TestClient

from app.models.common import Question
from app.services.question import QuestionService


def test_get_question_success(
    client: TestClient, sample_question_for_api: Question
) -> None:
    """Тест на успешное получение вопроса."""
    with patch("app.services.question.QuestionService.get_question") as mock_service:
        mock_service.return_value = sample_question_for_api
        question_id = sample_question_for_api.id
        response = client.get(f"/questions/{question_id}")
        mock_service.assert_called_once()
        assert response.status_code == 200

        data = response.json()
        assert data["text"] == sample_question_for_api.text
        assert "created_at" in data


def test_get_question_not_found(client: TestClient, nonexistent_id: int) -> None:
    """Тест на получение несуществующего вопроса."""
    with patch("app.services.question.QuestionService.get_question") as mock_service:
        mock_service.side_effect = HTTPException(
            status_code=404, detail="Вопрос не найден"
        )

        response = client.get(f"/questions/{nonexistent_id}")
        mock_service.assert_called_once()
        assert response.status_code == 404


def test_get_all_questions_success(mock_db: Mock) -> None:
    """Тест успешного получения всех вопросов."""
    mock_questions = [Mock(spec=Question), Mock(spec=Question)]
    mock_db.query.return_value.all.return_value = mock_questions

    result = QuestionService.get_all_questions(mock_db)

    assert result == mock_questions
    mock_db.query.assert_called_once_with(Question)


def test_get_all_questions_empty(mock_db: Mock) -> None:
    """Тест получения пустого списка вопросов."""
    mock_db.query.return_value.all.return_value = []

    result = QuestionService.get_all_questions(mock_db)

    assert result == []
    assert len(result) == 0
