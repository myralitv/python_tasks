from app.cycle.func_even_numbers import even_numbers
import pytest


@pytest.mark.parametrize('number1, number2, expected_result', [(2, 8, [2, 4, 6, 8]),
                                                               (-7, 9, [-6, -4, -2, 0, 2, 4, 6, 8]),
                                                               (-9, 14, [-8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14])])
def test_func_even_numbers(number1: int, number2: int, expected_result: int):
    assert even_numbers(number1, number2) == expected_result


@pytest.mark.parametrize("expected_exception, number1, number2", [(TypeError, "2", 6),
                                                                  (TypeError, 1.5, 10)])
def test_type_error(expected_exception, number1: int, number2: int):
    with pytest.raises(expected_exception):
        even_numbers(number1, number2)


def test_name_error():
    with pytest.raises(NameError):
        even_numbers(gd565, 4)