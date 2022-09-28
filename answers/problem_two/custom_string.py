"""
This module provides custom string support for problem_two
"""
import re


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
        self.string_part = re.search(r"(?<=\:\ )[a-z]{1,}$", line)[0]

        # Save the original line
        self.raw = line
