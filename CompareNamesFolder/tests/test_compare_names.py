#I test filen skriver jag
#from ..src.compare_names import compare_names
from CompareNamesFolder.src.compare_names import compare_names

def test_compare_names__input_is_not_a_string():
    expected = False
    actual = compare_names(123, "Olle")
    assert actual == expected

def test_compare_names__name_is_not_a_string():
    expected = False
    actual = compare_names("kal", 998)
    assert actual == expected

def test_compare_names__input_is_in_name():
    expected = True
    actual = compare_names("kal", "Kalle")
    assert actual == actual