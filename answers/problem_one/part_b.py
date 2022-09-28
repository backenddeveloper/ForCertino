"""
This module contains the code that satisfies part 1b of the technical test
"""
from answers.file import IntegerIterator


class PartB:
    """
    The solution to part 1b
    """

    def __init__(self, number_list: IntegerIterator):
        """
        :param input_iterator: An Iterator that provides the input for the solution
        """
        self.number_list = number_list

    def multiples(self) -> list[int]:
        """
        find_multiples finds pairs of numbers in the number_list
        that add up to 2020 and multiplies them together
        :return: A list of numbers, the multiples
        """

        return [(i[0] * i[1] * i[2]) for i in self.triplets()]

    def triplets(self) -> list[list[int]]:
        """
        find_number_triplets finds triplets of numbers in number_list
        that add up to 2020

        :param number_list: A generator or list that contains the input
        :return: A list of sorted triplets (each a list that adds up to 2020)

        The way it accomplishes this is by building a tree-like data
        structure out of associative dictionaries.

        {1 :
            {2 : 3},
            {4 : 5),
            ...
         2 :
            {3 : 4},
            {5 : 6},
            ...
        }
        As we check whether elements are less than 2020 before adding them
        to the tree, and given that paths in the tree are unique:
        The worst-case maximum number of elements in the tree is (2020 * 2020)

        It is expected to tend to this as N tends to infinity.

        As we loop over the number_list three times, it is expected to find
        all triplets in a number_list in O(3n * c) ~ O(n) time.
        It is also expected to use O(c) ~ O(1) allocated memory.

        The output list contains all couples seen, this grows proportionally
        to the number of valid inputs.
        """

        memory_allocation = {}

        for number in self.number_list:

            if number < 2020 and number not in memory_allocation:

                memory_allocation[number] = {}

        for second_number in self.number_list:

            for first_number in memory_allocation:

                if (second_number + first_number) < 2020:

                    if second_number not in memory_allocation[first_number]:

                        memory_allocation[first_number][second_number] = {}

        output = []

        for third_number in self.number_list:

            for first_number in memory_allocation:

                for second_number in memory_allocation[first_number]:

                    if 2020 == (first_number + second_number + third_number):

                        triplet = sorted([first_number, second_number, third_number])

                        if triplet not in output:

                            output.append(triplet)

        return output
