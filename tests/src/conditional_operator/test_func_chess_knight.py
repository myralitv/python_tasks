from src.conditional_operator.func_chess_knight import chess_knight
import pytest


@pytest.mark.parametrize('x1, y1, x2, y2, expected_result', [(4, 8, 6, 8, "Yes"),
                                                             (4, 8, 4, 1, "Yes"),
                                                             (4, 8, 9, 1, "No"),
                                                             (4, 8, 7, 1, "No")])
def test_func_chess_knight(x1: int, y1: int, x2: int, y2: int, expected_result: str):
    assert chess_knight(x1, y1, x2, y2) == expected_result


@pytest.mark.parametrize("exception, x1, y1, x2, y2", [(ValueError, -8, 4, 5, 4),
                                                       (ValueError, 4, -1, 4, 3),
                                                       (TypeError, "aaa", 2, 5, 3),
                                                       (TypeError, "5", "3", "5", "8")])
def test_type_error(exception, x1, y1, x2, y2):
    with pytest.raises(exception):
        chess_knight(x1, y1, x2, y2)


def test_name_error1():
    with pytest.raises(NameError):
        chess_knight(gd565, 4, 4, 1)


def test_name_error2():
    with pytest.raises(NameError):
        chess_knight(4, gb45, 2, 4)