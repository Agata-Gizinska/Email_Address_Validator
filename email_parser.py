"""
This module provides the definition of EmailParser class.
"""

import re
from email_address import EmailAddress


class EmailParser:
    """
    A class handling argument parser's functions, which perform operations
    on EmailAddress objects.

    Attributes:
    -------------
    valid : list
        A list of validated EmailAddress objects
    invalid : list
        A list of non-validated EmailAddress objects

    Methods:
    -------------
    __init__(self, valid_email_list, invalid_email_list)
    show_incorrect_emails(self)
    search_emails_by_text(self, text)
    group_emails_by_domain(self)
    find_emails_not_in_logs(self, path)
    """

    def __init__(self, valid_email_list, invalid_email_list):
        self.valid = valid_email_list
        self.invalid = invalid_email_list

    def show_incorrect_emails(self):
        """
        Print the number of invalid emails, then one invalid email per line.
        """
        incorrect_emails = [email for email in self.invalid]
        return incorrect_emails

    def search_emails_by_text(self, text: str):
        """
        Take a string argument and print the number of found emails, then
        one found email per line.

        Parameters
        -------------
        text : str
            A string representing the searched text
        """
        searched_text = text
        pattern = re.compile(searched_text)
        matches = []
        for email_address in (self.valid + self.invalid):
            if pattern.findall(email_address.email):
                matches.append(email_address.email)
        return matches

    def group_emails_by_domain(self):
        """
        Group emails by one domain and order domains and emails
        alphabetically.
        """
        email_dict = {}
        for email_address in self.valid:
            key = str(email_address.domain)
            value = str(email_address.email)
            if key not in email_dict:
                email_dict[key] = [value]
            elif isinstance(email_dict[key], list):
                email_dict[key].append(value)
            else:
                email_dict[key] = [email_dict[key], value]
        sorted_keys = sorted(email_dict)
        email_dict_sorted = {key: sorted(email_dict[key]) for
                             key in sorted_keys}
        return email_dict_sorted

    def find_emails_not_in_logs(self, path: str):
        """
        Find emails that are not in the provided logs file. Print
        the numbers of found emails, then one found email per line
        sorted alphabetically.

        Parameters
        -------------
        path : str
            A string representing a path to logs file
        """
        emails_from_logs = []
        emails_not_sent = []
        clean_lines = []
        with open(path, "r") as logs:
            lines = logs.readlines()
            for line in lines:
                clean_lines.append(line.rstrip(" \n"))
        pattern = re.compile(r'[\w.+-]+@[\w-]+\.[\w.-]+')
        for line in clean_lines:
            match = re.search(pattern, line)
            if match:
                email = EmailAddress(match[0])
                if email in self.valid:
                    emails_from_logs.append(email)
        for email in self.valid:
            if email not in emails_from_logs:
                emails_not_sent.append(email)
        emails_not_sent = sorted(emails_not_sent)
        return emails_not_sent
