from app.conditional_operator.func_maximum import maximum
import pytest


@pytest.mark.parametrize('a, b, expected_result', [(4, 8, 8),
                                                   (5, 7, 7),
                                                   (2, 20, 20),
                                                   (5, -5, 5)])
def test_func_maximum(a: int, b: int, expected_result: int):
    assert maximum(a, b) == expected_result


@pytest.mark.parametrize("expected_exception, number1, number2", [(TypeError, 5, "2"),
                                                                  (TypeError, "aaa", 2),
                                                                  (TypeError, "5", "-5"),
                                                                  (TypeError, 9.5, 2)])
def test_type_error(expected_exception, number1: int, number2: int):
    with pytest.raises(expected_exception):
        maximum(number1, number2)


def test_name_error1():
    with pytest.raises(NameError):
        maximum(gd565, 4)


def test_name_error2():
    with pytest.raises(NameError):
        maximum(4, gb45)

# def test_assertion_error():
#     with pytest.raises(AssertionError):
#         maximum("5", "-5")

# def test_func_maximum1():
#     assert maximum(5, 7) == 7

# def test_func_maximum2():
#     assert maximum(2, 20) == 20
