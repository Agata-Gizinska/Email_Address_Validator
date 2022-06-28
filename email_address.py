"""
This module provides the definition of EmailAddress class.
"""


class EmailAddress:
    """
    A class handling argument parser's functions, which perform operations
    on files containing email addresses and on EmailAddress objects.

    Attributes:
    -------------
    files : list
        A list of files containing email addresses
    valid : list
        A list of validated EmailAddress objects
    invalid : list
        A list of non-validated EmailAddress objects

    Methods:
    -------------
    __init__(self, email)
    __repr__(self)
    __eq__(self, other)
    __gt__(self, other)
    __lt__(self, other)
    _validate(self)
    """

    def __init__(self, email: str):
        self.email = email
        self.username = email.split("@")[0] if "@" in email else email
        self.domain = email.split("@")[1] if "@" in email else email
        self.validated = self._validate()

    def __repr__(self):
        return self.email

    def __eq__(self, other):
        return self.email == other.email

    def __gt__(self, other):
        return self.email > other.email

    def __lt__(self, other):
        return self.email < other.email

    def _validate(self):
        """
        A method performing a validation of EmailAddress object.

        Validity conditions:
        -------------
        1. there is only one "@";
        2. length of the part before the "@" is at least 1;
        3. length of the part between "@" and "." is at least 1;
        4. length of the part after the last "." is at least 1 and
        at most 4 and contains only letters and/or digits.
        """

        conditions = {
            "single_@": False,
            "one_char_before_@": False,
            "at_least_one_char_between_dot_and_@": False,
            "one_to_four_chars_after_last_dot": False
        }

        if "@" in self.email and self.email.count("@") == 1:
            conditions["single_@"] = True
        if len(self.username) >= 1:
            conditions["one_char_before_@"] = True
        if "." in self.domain:
            domain_split_list = self.domain.split(".")
            before_dot = domain_split_list[0]
            after_last_dot = domain_split_list[len(domain_split_list)-1]
            if len(before_dot) >= 1:
                conditions["at_least_one_char_between_dot_and_@"] = True
            if 1 <= len(after_last_dot) <= 4 and after_last_dot.isalnum():
                conditions["one_to_four_chars_after_last_dot"] = True

        if all(conditions.values()):
            return True

        return False
