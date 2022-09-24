from answers.problem_one.part_a import find_multiples as part_a
from answers.problem_one.part_a import find_number_couples
from answers.problem_one.part_b import find_multiples as part_b
from answers.problem_one.part_b import find_number_triplets


test_set = [
    1721,
    979,
    366,
    299,
    675,
    1456,
]


def test_part_a_acceptance():

    assert [514579] == part_a(test_set)


def test_part_a_finds_number_couples():

    assert [[299, 1721]] == find_number_couples(test_set)


def test_part_b_acceptance():

    assert [241861950] == part_b(test_set)


def test_part_b_find_number_triplets():

    assert [[366, 675, 979]] == find_number_triplets(test_set)
