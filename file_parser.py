"""
This module provides the definition of EmailFileParser class.
"""

import os
import csv
from pathlib import Path
from email_address import EmailAddress


class EmailFileParser:
    """
    A class performing operations on files with email addresses.

    Attributes:
    -------------
    email_filer_dir : str
        A string representing a path to the directory with email files
    files : list
        A list of files containing email addresses
    valid_emails : list
        A list of validated EmailAddress objects
    invalid_emails : list
        A list of non-validated EmailAddress objects

    Methods:
    -------------
    __init__(self, email_files_directory)
    get_files_list(self)
    parse_txt(self, txt_file_path)
    parse_csv(self, csv_file_path)
    get_emails_from_files(self)
    """

    def __init__(self, email_files_directory):
        self.email_files_dir = email_files_directory
        self.files = self.get_files_list()
        self.valid_emails, self.invalid_emails = self.get_emails_from_files()

    def get_files_list(self):
        """
        Return a list of paths to the files with email addresses.
        """
        files = []
        directory = self.email_files_dir
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            if os.path.isfile(f):
                files.append(f"{directory}{os.sep}{filename}")
        return files

    def parse_txt(self, txt_file_path):
        """Read email addresses from .txt files and return a list of
        EmailAddress objects."""
        results = []
        txt_file = open(txt_file_path, "r", encoding="utf-8")
        try:
            raw_lines = txt_file.readlines()
            clean_lines = [line.rstrip("\n") for line in raw_lines]
            for line in clean_lines:
                email_address = EmailAddress(line)
                results.append(email_address)
        except UnicodeDecodeError:
            txt_file.close()
        txt_file.close()
        return results

    def parse_csv(self, csv_file_path):
        """Read email addresses from .csv files and return a list of
        EmailAddress objects."""
        results = []
        csv_file = open(csv_file_path, "r", newline="", encoding="utf-8")
        reader = csv.DictReader(csv_file, delimiter=";")
        for row in reader:
            email = row["email"].rstrip("\n")
            email_address = EmailAddress(email)
            results.append(email_address)
        csv_file.close()
        return results

    def get_emails_from_files(self):
        """
        Get email addresses from files and divide them into two lists
        depending on objects being validated.
        """
        all_emails = []
        valid_emails = []
        invalid_emails = []
        for filepath in self.files:
            if Path(filepath).suffix == ".txt":
                for email in self.parse_txt(filepath):
                    all_emails.append(email)
            elif Path(filepath).suffix == ".csv":
                for email in self.parse_csv(filepath):
                    all_emails.append(email)
        for email_address in all_emails:
            if email_address.validated and email_address not in valid_emails:
                valid_emails.append(email_address)
            if not email_address.validated:
                invalid_emails.append(email_address)
        return valid_emails, invalid_emails
