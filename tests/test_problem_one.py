from answers.problem_one import part_a
from answers.problem_one import part_a_find_numbers


def _test_input_generator():

    for number in [
        1721,
        979,
        366,
        299,
        675,
        1456,
    ]:
        yield number

def test_part_a_acceptance():

    assert [514579] == part_a(_test_input_generator)


def test_part_a_finds_numbers():

    assert [299, 1721] == part_a_find_numbers(_test_input_generator)
