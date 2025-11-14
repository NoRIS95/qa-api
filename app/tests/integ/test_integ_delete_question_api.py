"""Интеграционные тесты для эндпоинта удаления вопроса."""

from fastapi.testclient import TestClient


def test_delete_question_success(client: TestClient, sample_question: dict) -> None:
    """Тест на успешное удаление вопроса."""
    question_id = sample_question["id"]
    response = client.delete(f"/questions/{question_id}")
    assert response.status_code == 200

    response = client.get(f"/questions/{question_id}")
    assert response.status_code == 404

def test_delete_question_invalid_id(client: TestClient) -> None:
    """Тест на удаление вопроса с неправильным форматом id."""
    question_id = "wrong_id"
    response = client.delete(f"/questions/{question_id}")
    assert response.status_code == 422

def test_delete_nonexistent_question(client: TestClient, nonexistent_id: int) -> None:
    """Тест на удаление несуществующего вопроса."""
    response = client.delete(f"/questions/{nonexistent_id}")
    assert response.status_code == 404

def test_cascade_delete(client: TestClient, sample_question: dict,
                         answer_data: dict) -> None:
    """Тест каскадного удаления вопроса с ответами."""
    question_id = sample_question['id']
    answer_response = client.post(f"/questions/{question_id}/answers/",
                                   json=answer_data)
    answer_id = answer_response.json()["id"]

    response = client.delete(f"/questions/{sample_question['id']}")
    assert response.status_code == 200

    response = client.get(f"/questions/{question_id}")
    assert response.status_code == 404

    response = client.get(f"/answers/{answer_id}")
    assert response.status_code == 404
