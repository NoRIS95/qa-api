"""Файл с общей фикстурой."""
import uuid

import pytest


@pytest.fixture
def answer_data() -> dict:
    """Фикстура данных для создания ответа."""
    return {
        "text": "Тестовый ответ на вопрос",
        "user_id": str(uuid.uuid4()),
    }
