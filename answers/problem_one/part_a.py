"""
This module contains the code that satisfies part 1a of the technical test
"""


def find_multiples(number_list) -> list[int]:
    """
    find_multiples finds pairs of numbers in the number_list
    that add up to 2020 and multiplies them together
    :param number_list: A generator or list that contains the input
    :return: A list of numbers, the multiples
    """
    solution_couples = find_number_couples(number_list)

    return [(i[0] * i[1]) for i in solution_couples]


def find_number_couples(number_list) -> list[list[int]]:
    """
    find_number_couples finds pairs of numbers in the number_list
    that add up to 2020

    :param number_list: A generator or list that contains the input
    :return: A list of sorted couples (each a list that adds up to 2020)

    The way it accomplishes this is by building a list of the numbers
    below 2020 that it has seen, then looks for compliments that add to 2020

    The worst-case maximum number of elements in the tree is 2020

    It is expected to tend to this as N tends to infinity.

    As we loop over the number_list twice, it is expected to find
    all triplets in a number_list in O(2n * c) ~ O(n) time.
    It is also expected to use O(c) ~ O(1) allocated memory.
    """

    memory_allocation = []

    for number in number_list:

        if number < 2020 and number not in memory_allocation:

            memory_allocation.append(number)

    output = []

    for number in number_list:

        if (2020 - number) in memory_allocation:

            couple = sorted((number, (2020 - number)))

            if couple not in output:

                output.append(couple)

    return output
