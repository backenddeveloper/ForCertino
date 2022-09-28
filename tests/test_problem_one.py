from answers.problem_one.part_a import PartA
from answers.problem_one.part_b import PartB


test_set = [
    1721,
    979,
    366,
    299,
    675,
    1456,
]


def test_part_a_acceptance():

    assert [514579] == PartA(test_set).multiples()


def test_part_a_finds_number_couples():

    assert [[299, 1721]] == PartA(test_set).couples()


def test_part_b_acceptance():

    assert [241861950] == PartB(test_set).multiples()


def test_part_b_find_number_triplets():

    assert [[366, 675, 979]] == PartB(test_set).triplets()
