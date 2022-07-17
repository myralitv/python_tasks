from app.cycle.func_divisor_of_number import divisor_of_number
import pytest


@pytest.mark.parametrize('number, expected_result', [(25, [1, 5, 25]),
                                                     (6, [1, 2, 3, 6]),
                                                     (7, [1, 7]),
                                                     (42, [1, 2, 3, 6, 7, 14, 21, 42])])
def test_func_divisor_of_number(number: int, expected_result: int):
    assert divisor_of_number(number) == expected_result


@pytest.mark.parametrize("expected_exception, number", [(TypeError, "2"),
                                                        (ValueError, -2)])
def test_type_error(expected_exception, number: int):
    with pytest.raises(expected_exception):
        divisor_of_number(number)


def test_name_error():
    with pytest.raises(NameError):
        divisor_of_number(gd565)


def test_zero_number():
    divisor_of_number(0)