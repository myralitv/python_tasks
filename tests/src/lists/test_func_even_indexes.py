from app.lists.func_even_indexes import even_indexes
import pytest


def test_func_even_indexes():
    assert even_indexes([1, 7, 6]) == [1, 6]


def test_func_even_indexes1():
    assert even_indexes([5, 10, 6, 11, 3, 8, 9, 7]) == [5, 6, 3, 9]


def test_type_error():
    with pytest.raises(TypeError):
        even_indexes(4)


def test_type_error1():
    with pytest.raises(TypeError):
        even_indexes('boat')


def test_type_error2():
    with pytest.raises(TypeError):
        even_indexes('goal')


def test_type_error3():
    with pytest.raises(TypeError):
        even_indexes('1', 6, 3)


def test_name_error():
    with pytest.raises(NameError):
        even_indexes(gd565)