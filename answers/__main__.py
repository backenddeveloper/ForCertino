"""
This is the main module entrypoint for running the answers
"""
from answers.file import IntegerIterator
from answers.problem_one.part_a import find_multiples as part_a
from answers.problem_one.part_b import find_multiples as part_b


input_1_filename = "problems/input1.txt"

input_2_filename = "problems/input2.txt"

if __name__ == "__main__":

    input_1_file_iterator = IntegerIterator(input_1_filename)

    multiples = part_a(input_1_file_iterator)
    print(f"The multiples of all pairs totalling 2020 in input1.txt are: {multiples}")  # noqa E501

    multiples = part_b(input_1_file_iterator)
    print(f"The multiples of all triplets totalling 2020 in input1.txt are: {multiples}")  # noqa E501
