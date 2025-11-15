"""Юнит-тесты для эндпоинта получения ответа."""

from unittest.mock import patch

from fastapi import HTTPException
from fastapi.testclient import TestClient

from app.models.common import Answer


def test_get_answer_success(client: TestClient, sample_answer_for_api: Answer) -> None:
    """Тест на успешное получение ответа."""
    with patch("app.services.answer.AnswerService.get_answer") as mock_service:
        mock_service.return_value = sample_answer_for_api
        answer_id = sample_answer_for_api.id
        response = client.get(f"/answers/{answer_id}")
        mock_service.assert_called_once()
        assert response.status_code == 200

        data = response.json()
        assert data["text"] == sample_answer_for_api.text
        assert "created_at" in data


def test_get_answer_not_found(client: TestClient, nonexistent_id: int) -> None:
    """Тест на получение несуществующего ответа."""
    with patch("app.services.answer.AnswerService.get_answer") as mock_service:
        mock_service.side_effect = HTTPException(
            status_code=404, detail="Ответ не найден"
        )

        response = client.get(f"/answers/{nonexistent_id}")
        mock_service.assert_called_once()
        assert response.status_code == 404
