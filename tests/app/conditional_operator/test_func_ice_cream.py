from app.conditional_operator.func_ice_cream import ice_cream
import pytest


@pytest.mark.parametrize('ice_ball, expected_result', [(8, "Yes"),
                                                       (3, "Yes"),
                                                       (5, "Yes"),
                                                       (4, "No"),
                                                       (7, "No"),
                                                       (9, "No")])
def test_func_chess_castle(ice_ball: int, expected_result: str):
    assert ice_cream(ice_ball) == expected_result


@pytest.mark.parametrize("exception, ice_ball", [(ValueError, -8),
                                                 (TypeError, "aaa")])
def test_type_error(exception, ice_ball):
    with pytest.raises(exception):
        ice_cream(ice_ball)


def test_name_error():
    with pytest.raises(NameError):
        ice_cream(gd565)