from answers.file import IntegerIterator


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
