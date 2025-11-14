"""Юнит-тесты для эндпоинта создания вопроса."""


from fastapi.testclient import TestClient


def test_create_question_valid(client: TestClient) -> None:
    """Тест на создание вопрос с валидными данными."""
    response = client.post("/questions/", json={"text": "Test questions"})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["text"] == "Test questions"
    assert "created_at" in data

def test_create_question_invalid_text(client: TestClient) -> None:
    """Тест на создание вопроса с невалидным text."""
    response = client.post("/questions/", json={"text": 123})
    assert response.status_code == 422

def test_create_question_empty_text(client: TestClient) -> None:
    """Тест на создание вопроса с пустым полем text."""
    response = client.post("/questions/", json={"text": None})
    assert response.status_code == 422

def test_create_question_empty_json(client: TestClient) -> None:
    """Тест на создание вопроса с пустыми данными."""
    response = client.post("/questions/", json={})
    assert response.status_code == 422
