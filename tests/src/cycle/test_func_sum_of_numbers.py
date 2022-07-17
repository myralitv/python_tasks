from app.cycle.func_sum_of_numbers import sum_of_numbers
import pytest


def test_func_sum_of_numbers():
    assert sum_of_numbers((2, 20)) == 22


def test_func_sum_of_numbers1():
    assert sum_of_numbers((2, 20, 5)) == 27


def test_func_sum_of_numbers2():
    assert sum_of_numbers((-6, -4, -2, 0, 2, 4, 6, 8)) == 8


def test_name_error():
    with pytest.raises(NameError):
        sum_of_numbers((gd565, 4))


def test_type_error():
    with pytest.raises(TypeError):
        sum_of_numbers(("gd565", 4))
