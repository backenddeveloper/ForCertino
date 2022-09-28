from answers.problem_two.solution import PartA
from answers.problem_two.solution import PartB


test_set = [
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc"
]


def test_part_a_acceptance():

    assert 2 == PartA(test_set).count()


def test_part_a_finds_valid_strings():

    valid_strings = list(PartA(test_set).valid_strings())

    assert "1-3 a: abcde" in valid_strings
    assert "2-9 c: ccccccccc" in valid_strings


def test_part_b_acceptance():

    assert 1 == PartB(test_set).count()


def test_part_b_finds_valid_strings():

    assert "1-3 a: abcde" in PartB(test_set).valid_strings()
