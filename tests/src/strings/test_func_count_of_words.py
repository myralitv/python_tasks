from src.strings.func_count_of_words import count_words
import pytest


def test_func_zero_in_list():
    assert count_words('Hi my name is Myroslav and I am 26') == 9


def test_func_zero_in_list1():
    assert count_words('Connected to cloud server via console') == 6


def test_type_error():
    with pytest.raises(TypeError):
        count_words(4)


def test_name_error():
    with pytest.raises(NameError):
        count_words(gd565)



