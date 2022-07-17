from app.cycle.func_count_of_divisor import count_divisor
import pytest


@pytest.mark.parametrize('number, expected_result', [(25, 3),
                                                     (6, 4),
                                                     (7, 2),
                                                     (42, 8)])
def test_func_count_of_divisor(number: int, expected_result: int):
    assert count_divisor(number) == expected_result


@pytest.mark.parametrize("expected_exception, number", [(TypeError, "2"),
                                                        (ValueError, -2)])
def test_type_error(expected_exception, number: int):
    with pytest.raises(expected_exception):
        count_divisor(number)


def test_name_error():
    with pytest.raises(NameError):
        count_divisor(gd565)


def test_zero_number():
    count_divisor(0)