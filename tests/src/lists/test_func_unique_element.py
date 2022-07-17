from app.lists.func_unique_element import unique_element
import pytest


def test_func_unique_element():
    assert unique_element([9, 2, 4, 6, 3, 6, 4, 8, 3]) == [9, 2, 8]


def test_func_unique_element1():
    assert unique_element([0, 4, 4, -1, 5, 9, 5, 8, 8]) == [0, -1, 9]


def test_type_error():
    with pytest.raises(TypeError):
        unique_element(4)


def test_type_error1():
    with pytest.raises(TypeError):
        unique_element('boat')


def test_type_error2():
    with pytest.raises(TypeError):
        unique_element(('1', 3, 6, 11, 9, 7, 9, 4))


def test_name_error():
    with pytest.raises(NameError):
        unique_element(gd565)