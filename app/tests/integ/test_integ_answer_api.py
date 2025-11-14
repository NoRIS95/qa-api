"""Юнит-тесты для эндпоинта создания ответа."""

import uuid

from fastapi.testclient import TestClient


def test_create_answer_valid(
    client: TestClient, sample_question: dict, answer_data: dict
) -> None:
    """Тест на создание ответа с валидными данными."""
    id_question = sample_question["id"]
    answer_data = {"text": "Тестовый ответ на вопрос", "user_id": str(uuid.uuid4())}
    response = client.post(f"/questions/{id_question}/answers/", json=answer_data)
    assert response.status_code == 200
    data = response.json()
    assert data["question_id"] == id_question
    assert "id" in data
    assert data["text"] == answer_data["text"]
    assert "user_id" in answer_data


def test_create_answer_invalid_text(
    client: TestClient, sample_question: dict, answer_data: dict
) -> None:
    """Тест на создание ответа с невалидным text."""
    id_question = sample_question["id"]
    answer_data["text"] = False
    response = client.post(f"/questions/{id_question}/answers/", json=answer_data)
    assert response.status_code == 422


def test_create_answer_invalid_question_id(
    client: TestClient, answer_data: dict
) -> None:
    """Тест на создание ответа с невалидным question_id."""
    id_question = "Wrong"
    answer_data["question_id"] = id_question
    response = client.post(f"/questions/{id_question}/answers/", json=answer_data)
    assert response.status_code == 422


def test_create_answer_invalid_user_id(
    client: TestClient, sample_question: dict, answer_data: dict
) -> None:
    """Тест на создание ответа с невалидным user_id."""
    id_question = sample_question["id"]
    answer_data["user_id"] = 124
    response = client.post(f"/questions/{id_question}/answers/", json=answer_data)
    assert response.status_code == 422


def test_create_answer_empty_text(
    client: TestClient, sample_question: dict, answer_data: dict
) -> None:
    """Тест на создание ответа с пустым text."""
    id_question = sample_question["id"]
    answer_data["text"] = None
    response = client.post(f"/questions/{id_question}/answers/", json=answer_data)
    assert response.status_code == 422


def test_create_answer_empty_question_id(client: TestClient, answer_data: dict) -> None:
    """Тест на создание ответа с пустым question_id."""
    id_question = None
    answer_data["question_id"] = id_question
    response = client.post(f"/questions/{id_question}/answers/", json=answer_data)
    assert response.status_code == 422


def test_create_answer_empty_user_id(
    client: TestClient, sample_question: dict, answer_data: dict
) -> None:
    """Тест на создание ответа с пустым user_id."""
    id_question = sample_question["id"]
    answer_data["user_id"] = None
    response = client.post(f"/questions/{id_question}/answers/", json=answer_data)
    assert response.status_code == 422


def test_create_answer_empty_data(client: TestClient, sample_question: dict) -> None:
    """Тест на создание ответа с пустым JSON."""
    id_question = sample_question["id"]
    answer_data = {}
    response = client.post(f"/questions/{id_question}/answers/", json=answer_data)
    assert response.status_code == 422


def test_create_answer_nonexistent_question(
    client: TestClient, answer_data: dict
) -> None:
    """Тест на создание ответа к несуществующему вопросу."""
    id_question = 82374682734628356
    response = client.post(f"/questions/{id_question}/answers/", json=answer_data)
    assert response.status_code == 404


def test_create_answer_invalid_endpoint(
    client: TestClient, sample_question: dict, answer_data: dict
) -> None:
    """Тест на создание ответа по неверному эндпоинту."""
    id_question = sample_question["id"]
    response = client.post(f"/questions_wrong/{id_question}/answers/", json=answer_data)
    assert response.status_code == 404
