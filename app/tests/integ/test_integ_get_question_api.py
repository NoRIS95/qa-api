"""Интеграционные тесты для эндпоинта получения вопроса."""

from fastapi.testclient import TestClient


def test_get_question_success(client: TestClient, sample_question: dict) -> None:
    """Тест на успешное получение вопроса."""
    question_id = sample_question["id"]
    response = client.get(f"/questions/{question_id}")
    assert response.status_code == 200

    data = response.json()
    assert "id" in data
    assert data["text"] == sample_question["text"]
    assert "created_at" in data

def test_get_question_invalid_id(client: TestClient) -> None:
    """Тест на получение вопроса с неправильным форматом id."""
    question_id = "wrong_id"
    response = client.get(f"/questions/{question_id}")
    assert response.status_code == 422

def test_get_question_nonexistent_id(client: TestClient, nonexistent_id: int) -> None:
    """Тест на получение несуществующего вопроса."""
    response = client.get(f"/questions/{nonexistent_id}")
    assert response.status_code == 404

def test_get_all_questions_success(client: TestClient) -> None:
    """Тест на успешное получение всех вопросов."""
    response = client.get("/questions/")
    assert response.status_code == 200
    assert len(response.json()) > 0
