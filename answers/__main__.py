"""
This is the main module entrypoint for running the answers
"""
from answers.file import IntegerIterator
from answers.file import CustomStringIterator
from answers.problem_one.part_a import find_multiples as part_one_a
from answers.problem_one.part_b import find_multiples as part_one_b
from answers.problem_two.part_a import find_valid_count as part_two_a
from answers.problem_two.part_b import find_valid_count as part_two_b


input_1_filename = "problems/input1.txt"

input_2_filename = "problems/input2.txt"

if __name__ == "__main__":

    input_1_file_iterator = IntegerIterator(input_1_filename)

    input_2_file_iterator = CustomStringIterator(input_2_filename)

    multiples = part_one_a(input_1_file_iterator)
    print(f"The multiples of all pairs totalling 2020 in input1.txt are: {multiples}")

    multiples = part_one_b(input_1_file_iterator)
    print(
        f"The multiples of all triplets totalling 2020 in input1.txt are: {multiples}"
    )

    multiples = part_two_a(input_2_file_iterator)
    print(f"The number of part 2a valid strings in input2.txt are: {multiples}")

    multiples = part_two_b(input_2_file_iterator)
    print(f"The number of part 2a valid strings in input2.txt are: {multiples}")
