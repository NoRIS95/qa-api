"""Юнит-тесты для эндпоинта создания ответа."""


from datetime import datetime
from unittest.mock import Mock, patch

from fastapi.testclient import TestClient

from app.models.common import Question


def test_create_answer_valid(client: TestClient,
                             sample_question: Question,
                             answer_data: dict) -> None:
    """Тест на создание ответа с валидными данными."""
    with patch('app.services.answer.AnswerService.create_answer') as mock_service:
        mock_answer = Mock()
        mock_answer.id = 1
        mock_answer.text = answer_data["text"]
        mock_answer.user_id = answer_data["user_id"]
        mock_answer.question_id = sample_question.id
        mock_answer.created_at = datetime.now()
        mock_service.return_value = mock_answer

        response = client.post(
            f"/questions/{sample_question.id}/answers/",
            json=answer_data
        )
        assert response.status_code == 200

def test_create_answer_invalid_user_id(client: TestClient,
                                       sample_question: Question,
                                       answer_data: dict) -> None:
    """Тест на создание ответа с невалидным user_id."""
    with patch('app.services.answer.AnswerService.create_answer') as mock_service:
        mock_answer = Mock()
        mock_answer.id = 1
        mock_answer.text = answer_data["text"]
        mock_answer.user_id = 123
        mock_answer.question_id = sample_question.id
        mock_answer.created_at = datetime.now()
        mock_service.return_value = mock_answer
    response = client.post("/questions/{sample_question.id}/answers/", json=answer_data)
    assert response.status_code == 422

def test_create_answer_invalid_text(client: TestClient,
                                    sample_question: Question,
                                    answer_data: dict) -> None:
    """Тест на создание ответа с невалидным текстом."""
    with patch('app.services.answer.AnswerService.create_answer') as mock_service:
        mock_answer = Mock()
        mock_answer.id = 1
        mock_answer.text = {"json":"ответ с неверным форматом"}
        mock_answer.user_id = answer_data["user_id"]
        mock_answer.question_id = sample_question.id
        mock_answer.created_at = datetime.now()
        mock_service.return_value = mock_answer
    response = client.post("/questions/{sample_question.id}/answers/", json=answer_data)
    assert response.status_code == 422


def test_create_answer_empty_text(client: TestClient,
                                  sample_question: Question,
                                  answer_data: dict) -> None:
    """Тест на создание ответа без текста."""
    with patch('app.services.answer.AnswerService.create_answer') as mock_service:
        mock_answer = Mock()
        mock_answer.id = 1
        mock_answer.text = None
        mock_answer.user_id = answer_data["user_id"]
        mock_answer.question_id = sample_question.id
        mock_answer.created_at = datetime.now()
        mock_service.return_value = mock_answer
    response = client.post("/questions/{sample_question.id}/answers/", json=answer_data)
    assert response.status_code == 422


def test_create_answer_empty_question_id(client: TestClient, answer_data: dict) -> None:
    """Тест на создание ответа без question_id."""
    with patch('app.services.answer.AnswerService.create_answer') as mock_service:
        mock_answer = Mock()
        mock_answer.id = 1
        mock_answer.text = answer_data["text"]
        mock_answer.user_id = answer_data["user_id"]
        mock_answer.question_id = None
        mock_answer.created_at = datetime.now()
        mock_service.return_value = mock_answer
    response = client.post("/questions/{sample_question.id}/answers/", json=answer_data)
    assert response.status_code == 422

def test_create_answer_empty_user_id(client: TestClient,
                                     sample_question: Question,
                                     answer_data: dict) -> None:
    """Тест на создание ответа без user_id."""
    with patch('app.services.answer.AnswerService.create_answer') as mock_service:
        mock_answer = Mock()
        mock_answer.id = 1
        mock_answer.text = answer_data["text"]
        mock_answer.user_id = None
        mock_answer.question_id = sample_question.id
        mock_answer.created_at = datetime.now()
        mock_service.return_value = mock_answer
    response = client.post("/questions/{sample_question.id}/answers/", json=answer_data)
    assert response.status_code == 422

def test_create_answer_empty_datetime(client: TestClient,
                                      sample_question: Question,
                                      answer_data: dict) -> None:
    """Тест на создание ответа без даты создания."""
    with patch('app.services.answer.AnswerService.create_answer') as mock_service:
        mock_answer = Mock()
        mock_answer.id = 1
        mock_answer.text = answer_data["text"]
        mock_answer.user_id = answer_data["user_id"]
        mock_answer.question_id = sample_question.id
        mock_answer.created_at = None
        mock_service.return_value = mock_answer
    response = client.post("/questions/{sample_question.id}/answers/", json=answer_data)
    assert response.status_code == 422


def test_create_answer_invalid_endpoint(client: TestClient, sample_question: Question,
                                        answer_data: dict) -> None:
    """Тест на создание ответа с неверным эндпоинтом."""
    with patch('app.services.answer.AnswerService.create_answer') as mock_service:
        mock_answer = Mock()
        mock_answer.id = 1
        mock_answer.text = answer_data["text"]
        mock_answer.user_id = answer_data["user_id"]
        mock_answer.question_id = sample_question.id
        mock_answer.created_at = datetime.now()
        mock_service.return_value = mock_answer

        response = client.post(
            f"/questions_wrong/{sample_question.id}/answers/",
            json=answer_data
        )
        assert response.status_code == 404

def test_create_answer_empty(client: TestClient) -> None:
    """Тест на создание ответа без данных."""
    response = client.post("/questions/{sample_question.id}/answers/", json={})
    assert response.status_code == 422
