import os
from unittest import TestCase
from Email_Address_Validator.file_parser import EmailFileParser


class TestEmailFileParser(TestCase):
    """
    A class providing tests for EmailFileParser class.
    """
    def setUp(self):
        """Set up an EmailFileParser object."""
        if "Email_Address_Validator" not in os.getcwd():
            for (root, dirs, files) in os.walk(os.getcwd(), topdown=True):
                if "Email_Address_Validator" in dirs:
                    os.chdir("Email_Address_Validator")
        self.parser = EmailFileParser(os.path.abspath("emails"))

    def test_get_file_list(self):
        """Test EmailFileParser get_file_list method."""
        file_list = self.parser.get_files_list()
        assert self.parser.files == file_list
        assert isinstance(file_list, list)

    def test_get_emails_from_files(self):
        """Test EmailFileParser get_emails_from_files method."""
        valid, invalid = self.parser.get_emails_from_files()
        assert len(
            self.parser.valid_emails +
            self.parser.invalid_emails) == len(valid + invalid)
        assert isinstance(valid, list)
        assert isinstance(invalid, list)
