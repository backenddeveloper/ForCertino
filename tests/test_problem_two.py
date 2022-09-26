from answers.file import CustomString
from answers.problem_two.part_a import find_valid_count as part_a
from answers.problem_two.part_a import find_valid_strings as part_a_strings
from answers.problem_two.part_b import find_valid_count as part_b
from answers.problem_two.part_b import find_valid_strings as part_b_strings


test_set = [
    CustomString(s) for s in ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
]


def test_part_a_acceptance():

    assert 2 == part_a(test_set)


def test_part_a_finds_valid_strings():

    valid_strings = list(part_a_strings(test_set))

    assert "1-3 a: abcde" in valid_strings
    assert "2-9 c: ccccccccc" in valid_strings


def test_part_b_acceptance():

    assert 1 == part_b(test_set)


def test_part_b_finds_valid_strings():

    valid_strings = list(part_b_strings(test_set))

    assert "1-3 a: abcde" in valid_strings
