"""Юнит-тесты для эндпоинта удаления ответа."""

from unittest.mock import Mock, patch

import pytest
from fastapi import HTTPException

from app.models.common import Answer
from app.services.answer import AnswerService


def test_delete_answer_success(mock_db: Mock) -> None:
    """Тест успешного удаления ответа."""
    mock_answer = Mock(spec=Answer)

    with patch.object(AnswerService, "get_answer", return_value=mock_answer):
        result = AnswerService.delete_answer(mock_db, 1)

    mock_db.delete.assert_called_once_with(mock_answer)
    mock_db.commit.assert_called_once()
    assert result == mock_answer


def test_delete_answer_not_found(mock_db: Mock, nonexistent_id: int) -> None:
    """Тест удаления несуществующего ответа."""
    with patch.object(
        AnswerService, "get_answer", side_effect=HTTPException(404, "Not found")
    ):
        with pytest.raises(HTTPException) as exc_info:
            AnswerService.delete_answer(mock_db, nonexistent_id)

        assert exc_info.value.status_code == 404
        mock_db.delete.assert_not_called()
        mock_db.commit.assert_not_called()
