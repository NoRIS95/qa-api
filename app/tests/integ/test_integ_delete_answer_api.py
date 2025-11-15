"""Интеграционные тесты для эндпоинта удаления ответа."""

from fastapi.testclient import TestClient


def test_delete_answer_success(client: TestClient, sample_answer: dict) -> None:
    """Тест на успешное удаление ответа."""
    answer_id = sample_answer["id"]
    response = client.delete(f"/answers/{answer_id}")
    assert response.status_code == 200

    response = client.get(f"/answers/{answer_id}")
    assert response.status_code == 404


def test_delete_answer_invalid_id(client: TestClient) -> None:
    """Тест на удаление ответа с неправильным форматом id."""
    answer_id = "wrong_id"
    response = client.delete(f"/answers/{answer_id}")
    assert response.status_code == 422


def test_delete_nonexistent_answer(client: TestClient, nonexistent_id: int) -> None:
    """Тест на удаление несуществующего ответа."""
    response = client.delete(f"/answers/{nonexistent_id}")
    assert response.status_code == 404
