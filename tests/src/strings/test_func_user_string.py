from src.strings.func_user_string import user_string
import pytest


def test_func_zero_in_list():
    assert user_string('winterborn') == ('n', 'r', 'winte', 'winterbo', 'wnebr', 'itron', 'nrobretniw', 10)


def test_func_zero_in_list1():
    assert user_string('welcome') == ('l', 'm', 'welco', 'welco', 'wloe', 'ecm', 'emoclew', 7)


def test_type_error():
    with pytest.raises(TypeError):
        user_string(4)


def test_name_error():
    with pytest.raises(NameError):
        user_string(gd565)


def test_value_error():
    with pytest.raises(ValueError):
        user_string('boat')


def test_value_error1():
    with pytest.raises(ValueError):
        user_string('goal')