"""
This module contains the code that satisfies part 2a of the technical test
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

        if line.first_number <= line.string_part.count(line.given_letter):

            if line.second_number >= line.string_part.count(line.given_letter):

                # At this point we want the CustomString object to fall out of scope
                raw = line.raw
                del line
                yield raw
