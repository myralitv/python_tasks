from app.lists.func_elements_reverse import elements_reverse
import pytest


def test_func_element_reverse():
    assert elements_reverse([-1, 0, 1]) == [1, 0, -1]


def test_func_element_reverse1():
    assert elements_reverse([5, 10, 6, 11, 3, 8, 9, 7]) == [7, 9, 8, 3, 11, 6, 10, 5]


def test_type_error():
    with pytest.raises(TypeError):
        elements_reverse(4)


def test_type_error1():
    with pytest.raises(TypeError):
        elements_reverse('boat')


def test_type_error2():
    with pytest.raises(TypeError):
        elements_reverse('goal')


def test_type_error3():
    with pytest.raises(TypeError):
        elements_reverse('1', 6, 3)


def test_name_error():
    with pytest.raises(NameError):
        elements_reverse(gd565)
