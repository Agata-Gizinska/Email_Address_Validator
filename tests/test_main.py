"""
This module provides tests for the main program.
"""

import os
import pytest
from unittest import TestCase
from unittest.mock import patch
from Email_Address_Validator.main import main
from Email_Address_Validator.email_address import EmailAddress
from Email_Address_Validator.email_parser import EmailParser


class TestMain(TestCase):
    """
    A class providing tests for main program.
    """

    @classmethod
    def setUpClass(cls):
        """Set up a list of emails for all tests."""
        email_addresses = [
            "esidisi@hotmail.com",
            "g.giovanna@passione.it",
            "joseph.j@ovdr.com",
            "jotaro.qjo@gmail.com",
            "trish.una15@hotmail.com"
        ]
        cls.emails = []
        for email in email_addresses:
            cls.emails.append(EmailAddress(email))

    def setUp(self):
        """Set up an EmailParser object with mocked emails."""
        self.email_parser = EmailParser(self.emails, [])

    @pytest.fixture(autouse=True)
    def capfd(self, capfd):
        """Enable the retrieval of statements printed during tests."""
        self.capfd = capfd

    @patch("main.EmailFileParser.get_emails_from_files")
    def test_incorrect_emails(self, mock_emails):
        """Test --incorrect-emails argument parser flag."""
        test_params = ['--incorrect-emails']
        mock_emails.return_value = self.emails, []
        main(test_params)
        captured = self.capfd.readouterr()
        assert "Invalid emails (0):" in captured.out

    @patch("main.EmailFileParser.get_emails_from_files")
    def test_search_emails_by_text(self, mock_emails):
        """Test --search <string> argument parser flag."""
        test_params = ['--search', 'gio']
        mock_emails.return_value = self.emails, []
        main(test_params)
        captured = self.capfd.readouterr()
        assert "Found emails with 'gio' in email (1):" in captured.out
        assert "g.giovanna@passione.it" in captured.out

    @patch("main.EmailFileParser.get_emails_from_files")
    def test_group_by_domain(self, mock_emails):
        """Test --group-by-domain argument parser flag."""
        test_params = ['--group-by-domain']
        mock_emails.return_value = self.emails, []
        main(test_params)
        captured = self.capfd.readouterr()
        assert "Domain hotmail.com (2):" in captured.out
        assert "Domain gmail.com (1):" in captured.out
        assert "Domain passione.it (1):" in captured.out
        assert "Domain ovdr.com (1):" in captured.out
        for email in self.emails:
            assert email.email in captured.out

    @patch("main.EmailFileParser.get_emails_from_files")
    def test_find_emails_not_in_logs(self, mock_emails):
        """Test --find-emails-not-in-logs <path> argument parser flag."""
        path = os.path.abspath("email-sent.logs")
        test_params = ['-feil', path]
        mock_emails.return_value = self.emails, []
        main(test_params)
        captured = self.capfd.readouterr()
        assert "Emails not sent (5):" in captured.out
        for email in self.emails:
            assert email.email in captured.out
