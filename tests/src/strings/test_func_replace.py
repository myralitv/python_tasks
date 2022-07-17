from app.strings.func_replace import func_replace
import pytest


def test_func_zero_in_list():
    assert func_replace('ye11ow') == 'yeoneoneow'


def test_func_zero_in_list1():
    assert func_replace('we1come') == 'weonecome'


def test_type_error():
    with pytest.raises(TypeError):
        func_replace(4)


def test_name_error():
    with pytest.raises(NameError):
        func_replace(gd565)


def test_value_error():
    with pytest.raises(ValueError):
        func_replace('boat')


def test_value_error1():
    with pytest.raises(ValueError):
        func_replace('goal')