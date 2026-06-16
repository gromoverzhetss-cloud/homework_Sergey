import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, expected", [("sergey", "Sergey")])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, expected", [(" Sergey", "Sergey")])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, simbol, expected", [
    ("Sergey", "e", True),
    ("Sergey", "w", False)
    ])
def test_contains_positive(input_str, simbol, expected):
    assert string_utils.contains(input_str, simbol) == expected


@pytest.mark.positive_test
@pytest.mark.parametrize("string, simbol, expected", [
    ("Homework", "work", "Home")
])
def test_delete_symbol(string, simbol, expected):
    assert string_utils.delete_symbol(string, simbol) == expected
# @pytest.mark.negative
# @pytest.mark.parametrize("input_str, expected", [
#     ("123abc", "123abc"),
#     ("", ""),
#     ("   ", "   "),
# ])
# def test_capitalize_negative(input_str, expected):
#     assert string_utils.capitalize(input_str) == expected
