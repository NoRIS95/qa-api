"""Интеграционные тесты для эндпоинта получения ответа."""

from fastapi.testclient import TestClient


def test_get_answer_success(client: TestClient, sample_answer: dict) -> None:
    """Тест на успешное получение ответа."""
    answer_id = sample_answer["id"]
    response = client.get(f"/answers/{answer_id}")
    assert response.status_code == 200

    data = response.json()
    assert "id" in data
    assert data["text"] == sample_answer["text"]
    assert "created_at" in data


def test_get_answer_invalid_id(client: TestClient) -> None:
    """Тест на получение ответа с неправильным форматом id."""
    answer_id = "wrong_id"
    response = client.get(f"/answers/{answer_id}")
    assert response.status_code == 422


def test_get_answer_nonexistent_id(client: TestClient, nonexistent_id: int) -> None:
    """Тест на получение несуществующего ответа."""
    response = client.get(f"/answers/{nonexistent_id}")
    assert response.status_code == 404
