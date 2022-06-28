"""
This module provides tests for the EmailParser class.
"""

import os
import re
from unittest import TestCase
from Email_Address_Validator.email_address import EmailAddress
from Email_Address_Validator.email_parser import EmailParser


class TestEmailParser(TestCase):
    """
    A class providing tests for EmailParser class.
    """
    @classmethod
    def setUpClass(cls):
        """Set up a list of emails for all tests."""
        email_addresses = [
            "esidisi@hotmail.com",
            "g.giovanna@passione.it",
            "@ovdr.com",
            "jotaro.qjo@gmail.com",
            "trish.una15@hotmail.com"
        ]
        cls.valid_emails = []
        cls.invalid_emails = []
        for email in email_addresses:
            email_address = EmailAddress(email)
            if email_address.validated:
                cls.valid_emails.append(email_address)
            else:
                cls.invalid_emails.append(email_address)

    def setUp(self):
        """Set up an EmailParser object."""
        self.parser = EmailParser(self.valid_emails, self.invalid_emails)

    def test_show_incorrect_emails(self):
        """Test EmailParser incorrect_emails method."""
        incorrect_emails = self.parser.show_incorrect_emails()
        assert isinstance(incorrect_emails, list)
        for email in incorrect_emails:
            assert not email.validated

    def test_search_emails_by_text(self):
        """Test EmailParser search_emails_by_text method."""
        searched_text = "agustin"
        matches = self.parser.search_emails_by_text(searched_text)
        assert isinstance(matches, list)
        for email_address in matches:
            assert "agustin" in email_address

    def test_group_emails_by_domain(self):
        """Test EmailParser group_emails_by_domain method."""
        grouped_emails = self.parser.group_emails_by_domain()
        assert isinstance(grouped_emails, dict)
        for key, values in grouped_emails.items():
            for value in values:
                assert key in value
                assert value in [i.email for i in (self.parser.valid +
                                                   self.parser.invalid)]

    def test_find_emails_not_in_logs(self):
        """Test EmailParser find_emails_not_in_logs method."""
        if "Email_Address_Validator" not in os.getcwd():
            for (root, dirs, files) in os.walk(os.getcwd(), topdown=True):
                if "Email_Address_Validator" in dirs:
                    os.chdir("Email_Address_Validator")
        path = os.path.abspath("email-sent.logs")
        pattern = re.compile(r'[\w.+-]+@[\w-]+\.[\w.-]+')
        emails_not_sent = self.parser.find_emails_not_in_logs(path)
        assert isinstance(emails_not_sent, list)
        for email in emails_not_sent:
            assert re.match(pattern, email.email)
