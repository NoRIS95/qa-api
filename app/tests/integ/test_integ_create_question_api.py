"""Интеграционные тесты для эндпоинта создания вопроса."""

from fastapi.testclient import TestClient


def test_create_question_success(client: TestClient, question_data: dict) -> None:
    """Тест на успешное создание вопроса."""
    response = client.post("/questions/", json=question_data)
    assert response.status_code == 200

    data = response.json()
    assert "id" in data
    assert data["text"] == question_data["text"]
    assert "created_at" in data


def test_create_question_invalid_text(client: TestClient, question_data: dict) -> None:
    """Тест на создание вопроса с невалидным text."""
    question_data["text"] = False
    response = client.post("/questions/", json=question_data)
    assert response.status_code == 422


def test_create_question_empty_text(client: TestClient, question_data: dict) -> None:
    """Тест на создание вопроса с пустым полем text."""
    question_data["text"] = None
    response = client.post("/questions/", json=question_data)
    assert response.status_code == 422


def test_create_question_empty_json(client: TestClient) -> None:
    """Тест на создание вопроса с пустыми данными."""
    response = client.post("/questions/", json={})
    assert response.status_code == 422
