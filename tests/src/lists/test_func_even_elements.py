from src.lists.func_even_elements import even_elements
import pytest


def test_func_even_element():
    assert even_elements((5, 10, 6, 11, 3, 8, 9, 7)) == [10, 6, 8]


def test_func_even_element1():
    assert even_elements((1, 3, 6, 11, 9, 7, 9, 4)) == [6, 4]


def test_type_error():
    with pytest.raises(TypeError):
        even_elements(4)


def test_type_error1():
    with pytest.raises(TypeError):
        even_elements('boat')


def test_type_error2():
    with pytest.raises(TypeError):
        even_elements(('1', 3, 6, 11, 9, 7, 9, 4))


def test_name_error():
    with pytest.raises(NameError):
        even_elements(gd565)