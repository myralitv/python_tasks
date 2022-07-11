from src.lists.func_max_elem_index import max_index_elements
import pytest


def test_func_max_index_element():
    assert max_index_elements((5, 10, 6, 11, 3, 8, 19, 7)) == (19, 6)


def test_func_max_index_element1():
    assert max_index_elements((1, 3, 6, 11, 9, 7, 9, 4)) == (11, 3)


def test_type_error():
    with pytest.raises(TypeError):
        max_index_elements(4)


def test_type_error1():
    with pytest.raises(TypeError):
        max_index_elements('boat')


def test_type_error2():
    with pytest.raises(TypeError):
        max_index_elements(('1', 3, 6, 11, 9, 7, 9, 4))


def test_name_error():
    with pytest.raises(NameError):
        max_index_elements(gd565)