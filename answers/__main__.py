"""
This is the main module entrypoint for running the answers
"""
from answers.file import Iterator
from answers.file import IntegerIterator
from answers.problem_one.part_a import PartA as PartOneA
from answers.problem_one.part_b import PartB as PartOneB
from answers.problem_two.solution import PartA as PartTwoA
from answers.problem_two.solution import PartB as PartTwoB


INPUT_1_FILENAME = "problems/input1.txt"

INPUT_2_FILENAME = "problems/input2.txt"

if __name__ == "__main__":

    input_1_file_iterator = IntegerIterator(INPUT_1_FILENAME)

    input_2_file_iterator = Iterator(INPUT_2_FILENAME)

    multiples = PartOneA(input_1_file_iterator).multiples()
    print(f"The multiples of all pairs totalling 2020 in input1.txt are: {multiples}")

    multiples = PartOneB(input_1_file_iterator).multiples()
    print(
        f"The multiples of all triplets totalling 2020 in input1.txt are: {multiples}"
    )

    multiples = PartTwoA(input_2_file_iterator).count()
    print(f"The number of part 2a valid strings in input2.txt are: {multiples}")

    multiples = PartTwoB(input_2_file_iterator).count()
    print(f"The number of part 2a valid strings in input2.txt are: {multiples}")
