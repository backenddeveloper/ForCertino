"""
This module contains the code that satisfies part 2b of the technical test
"""
from typing import Generator
from answers.file import CustomString
from answers.file import CustomStringIterator


def find_valid_count(string_list: list[CustomString]) -> int:
    """
    This function runs find_valid_strings on the input list and counts the outputs
    It is a bit like len(find_valid_strings...)
    """
    return sum(1 for i in find_valid_strings(string_list))


def find_valid_strings(string_list: CustomStringIterator) -> Generator:
    """
    find_valid_strings takes a CustomStringIterator, checks its validity and yields its
    original raw value
    """
    for line in string_list:

        # Is the given letter in the first position
        first = bool(line.given_letter == line.string_part[line.first_number - 1])

        # Is the given letter in the second position
        second = bool(line.given_letter == line.string_part[line.second_number - 1])

        # This is the easiest way to do XOR in Python
        # A compaction of (first and not second) or (second and not first)
        if first != second:

            # At this point we want the CustomString object to fall out of scope
            raw = line.raw
            del line
            yield raw
