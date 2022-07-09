from src.conditional_operator.func_leap_year import leap_year
import pytest


@pytest.mark.parametrize("year, expected_result", [(2020, "Yes"),
                              (2022, "No"),
                              (999, "No")])
def test_func_leap_year(year: int, expected_result: str):
    assert leap_year(year) == expected_result


@pytest.mark.parametrize("expected_exeption, year", [(TypeError, "2020"),
                                                     (TypeError, "999")])
def test_type_error(expected_exeption, year):
    with pytest.raises(expected_exeption):
        leap_year(year)

def test_assertion_error():
    with pytest.raises(NameError):
        leap_year(gd565)
