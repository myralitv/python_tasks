from app.sort.func_sort_number import sort_number
import pytest


def test_func_sort_number():
    assert sort_number([0, 4, 9, -1, -8, 3, 7, 12, -20]) == [-20, -8, -1, 0, 3, 4, 7, 9, 12]


def test_func_sort_number1():
    assert sort_number([1.5, 6, 1, -1.7, 10, 2, 8, 12, -20]) == [-20, -1.7, 1, 1.5, 2, 6, 8, 10, 12]


def test_type_error():
    with pytest.raises(TypeError):
        sort_number(4)


def test_type_error1():
    with pytest.raises(TypeError):
        sort_number('boat')


def test_type_error2():
    with pytest.raises(TypeError):
        sort_number(('1', 3, 6, 11, 9, 7, 9, 4))


def test_name_error():
    with pytest.raises(NameError):
        sort_number(gd565)