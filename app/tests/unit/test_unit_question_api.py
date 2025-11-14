"""Юнит-тесты для эндпоинта создания вопроса."""

from datetime import datetime
from unittest.mock import Mock, patch

from fastapi.testclient import TestClient


def test_create_question_valid(client: TestClient) -> None:
    """Тест на создание вопроса с валидными данными."""
    with patch("app.services.question.QuestionService.create_question") as mock_service:
        mock_question = Mock()
        mock_question.id = 1
        mock_question.text = "Test question"
        mock_question.created_at = datetime.now()
        mock_question.answers = []
        mock_service.return_value = mock_question

        response = client.post("/questions/", json={"text": "Test questions"})
        assert response.status_code == 200
        data = response.json()
        assert data["text"] == "Test question"
        assert "created_at" in data


def test_create_question_invalid_id(client: TestClient) -> None:
    """Тест на создание вопроса с неверным типом id."""
    response = client.post("/questions/", json={"id": "Wrong id"})
    assert response.status_code == 422


def test_create_question_empty_id(client: TestClient) -> None:
    """Тест на создание вопроса с пустым id."""
    response = client.post("/questions/", json={"id": None})
    assert response.status_code == 422


def test_create_question_invalid_text(client: TestClient) -> None:
    """Тест на создание вопроса с неверным типом text."""
    response = client.post("/questions/", json={"text": False})
    assert response.status_code == 422


def test_create_question_empty_text(client: TestClient) -> None:
    """Тест на создание вопроса с пустым text."""
    response = client.post("/questions/", json={"text": None})
    assert response.status_code == 422


def test_create_question_invalid_datetime(client: TestClient) -> None:
    """Тест на создание вопроса с неверной датой."""
    response = client.post("/questions/", json={"created_at": 12345})
    assert response.status_code == 422


def test_create_question_empty_json(client: TestClient) -> None:
    """Тест на создание вопроса с пустыми данными."""
    response = client.post("/questions/", json={})
    assert response.status_code == 422


def test_create_question_not_found(client: TestClient) -> None:
    """Тест на создание вопроса со статусом 404."""
    with patch("app.services.question.QuestionService.create_question") as mock_service:
        mock_question = Mock()
        mock_question.id = 1
        mock_question.text = "Test question"
        mock_question.created_at = datetime.now()
        mock_question.answers = []
        mock_service.return_value = mock_question

        response = client.post("/questions_wrong/", json={"text": "Test questions"})
        assert response.status_code == 404
