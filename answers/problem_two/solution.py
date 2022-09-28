"""
This module contains the code that satisfies part 2b of the technical test
"""
from abc import ABC
from typing import Generator
from answers.file import Iterator
from answers.problem_two.custom_string import CustomString


class Solution(ABC):
    """
    This parent class that DRYs the solutions to PartA and PartB
    """

    def __init__(self, string_list: Iterator):
        """
        :param string_list: An Iterator such as a file Iterator containing the input
        """
        self.string_list = string_list

    def count(self) -> int:
        """
        This function runs find_valid_strings on the input list and counts the outputs
        It is a bit like len(find_valid_strings...)
        :return: A count of valid strings in the class input
        """
        return sum(1 for i in self.valid_strings())


class PartA(Solution):
    """
    This represents the solution to PartA of the exercise
    """

    def valid_strings(self) -> Generator:
        """
        find_valid_strings takes a CustomStringIterator, checks its validity and yields its
        original raw value
        :return: A Generator containing a list of valid strings
        """
        for line in self.string_list:

            # This will error if the input line is invalid
            line = CustomString(line)

            # if the count of the given letter in the string is greater than or
            # equal to the first number
            if line.first_number <= line.string_part.count(line.given_letter):

                # if the count of the given letter in the string is less than or
                # equal to the second number
                if line.second_number >= line.string_part.count(line.given_letter):

                    # At this point we want the CustomString object to fall out of
                    # scope, this will happen when it is disregarded by the consumer
                    yield line.raw


class PartB(Solution):
    """
    This represents the solution to PartB of the exercise
    """

    def valid_strings(self) -> Generator:
        """
        find_valid_strings takes a [File]Iterator, checks each line's validity
        first as a processable string, then as satisfying the requirements
        and yields its original raw value
        """
        for line in self.string_list:

            # This will error if the input line is invalid
            line = CustomString(line)

            # Is the given letter in the first position
            first = bool(line.given_letter == line.string_part[line.first_number - 1])

            # Is the given letter in the second position
            second = bool(line.given_letter == line.string_part[line.second_number - 1])

            # This is the easiest way to do XOR in Python
            # A compaction of (first and not second) or (second and not first)
            if first != second:

                # At this point we want the CustomString object to fall out of
                # scope, this will happen when it is disregarded by the consumer
                yield line.raw
