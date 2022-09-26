"""
The purpose of this module is to define a file-reading generator,
so as to reduce the total big-O memory usage reading the input.
"""
import re


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
        with open(self.filename, "r") as file:

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


class CustomString:
    """
    A CustomString holds a custom string from problem2 split into parts
    [https://pythex.org/] is your friend for Regex
    """

    def __init__(self, line: str):

        # an example is 11-14 j: jxjjjjjjtjjjjjv
        if not re.match(r"^\d{1,}[-]{1}\d{1,}\ [a-z]{1}\:\ [a-z]{1,}$", line):

            raise Exception(f"invalid line encountered: {line}")

        # 11 in above example
        self.first_number = int(re.search(r"^\d{1,}(?=[-])", line)[0])

        # 14 in above example
        self.second_number = int(re.search(r"(?<=[-])\d{1,}(?=\ )", line)[0])

        # j in the above example
        self.given_letter = re.search(r"(?<=[\d]\ )[a-z]{1}(?=\:)", line)[0]

        # jxjjjjjjtjjjjjv in the above example
        self.string_part = re.search(r"(?<=\:\ )[a-z]{1,}", line)[0]

        # Save the original line
        self.raw = line


class CustomStringIterator(Iterator):
    """
    CustomStringIterator is a special case of Iterator,
    it uses Rexep to validate and then split the custom strings for part two
    """

    def __iter__(self):
        """
        This yields a CustomString definition object for each line in the file
        """
        for line in super().__iter__():

            yield CustomString(line)
