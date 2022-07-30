from app.strings.func_cut_the_h import cut_h
import pytest


def test_func_zero_in_list():
    assert cut_h('1234hmvekh567890') == '1234567890'


def test_func_zero_in_list1():
    assert cut_h('welh1234567890hcome') == 'welcome'


def test_type_error():
    with pytest.raises(TypeError):
        cut_h(4)


def test_name_error():
    with pytest.raises(NameError):
        cut_h(gd565)


def test_value_error():
    with pytest.raises(ValueError):
        cut_h('1234mvekh567890')


def test_value_error1():
    with pytest.raises(ValueError):
        cut_h('welh1234567890come')