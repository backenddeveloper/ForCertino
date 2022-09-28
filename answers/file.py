"""
The purpose of this module is to define a file-reading generator,
so as to reduce the total big-O memory usage reading the input.
"""


class Iterator:
    """
    Iterator is an iterator rather than a Generator,
    but performs the same function for our usecase
    """

    def __init__(self, filename: str):
        """
        Construct a new file Iterator
        "param filename: The name of the file on disk to read
        """
        self.filename = filename

    def __iter__(self):
        """
        Read each line in the file
        """
        with open(self.filename, "r", encoding='ASCII') as file:

            for line in file:

                yield line


class IntegerIterator(Iterator):
    """
    IntegerIterator is a special case of Iterator,
    which casts each line to an Integer to sanitize input
    """

    def __iter__(self):
        """
        This will error if one of the lines is not readable as an Integer
        """
        for line in super().__iter__():

            yield int(line)
