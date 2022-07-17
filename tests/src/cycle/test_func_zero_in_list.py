from app.cycle.func_zero_in_list import zero_in_list
import pytest


def test_func_zero_in_list():
    assert zero_in_list((2, 0)) == 'Yes'


def test_func_zero_in_list():
    assert zero_in_list((2, 20, 5)) == 'No'


def test_func_zero_in_list():
    assert zero_in_list((-6, -4, -2, 0, 2, 4, 6, 8)) == 'Yes'


def test_name_error():
    with pytest.raises(NameError):
        zero_in_list((gd565, 4))


def test_type_error():
    with pytest.raises(TypeError):
        zero_in_list(("gd565", 4))