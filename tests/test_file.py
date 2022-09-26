from answers.file import IntegerIterator
from answers.file import CustomString
from answers.file import CustomStringIterator


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


def test_iterator_reads_input2():

    iterator = CustomStringIterator("problems/input2.txt")

    # The iterator returns CustomStrings
    for element in iterator:
        assert isinstance(element, CustomString)

    # 1000 custom strings in the file
    assert 1000 == len(list(iterator))
