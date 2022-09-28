import pytest
from answers.file import Iterator
from answers.file import IntegerIterator
from answers.problem_two.custom_string import CustomString


def test_iterator_reads_input1():

    iterator = IntegerIterator("problems/input1.txt")

    # 200 numbers in the file
    assert 200 == len(list(iterator))

    # first number in file
    assert 1440 in list(iterator)

    # arbitary number in middle of file
    assert 1761 in list(iterator)

    # last number in file
    assert 1925 in list(iterator)


def test_custom_string_seperates_correctly():

    line = "1-3 a: abcde"
    custom_string = CustomString(line)
    assert 1 == custom_string.first_number
    assert 3 == custom_string.second_number
    assert "a" == custom_string.given_letter
    assert "abcde" == custom_string.string_part


def test_custom_string_rejects_invalid_input():

    invalid_line = 'some invalid line of text'

    with pytest.raises(Exception):

        CustomString(invalid_line)


def test_iterator_reads_input2():

    iterator = Iterator("problems/input2.txt")

    strings = [CustomString(i) for i in iterator]

    # 1000 lines in file
    assert 1000 == len(strings)
