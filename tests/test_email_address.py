"""
This module provides tests for the EmailAddress class.
"""

from unittest import TestCase
from Email_Address_Validator.email_address import EmailAddress


class TestEmailAddress(TestCase):
    """
    A class providing tests for EmailAddress class.
    """

    def test_creation(self):
        """Test EmailAddress init method."""
        valid_email = EmailAddress("abc@domain.com")
        assert valid_email.email == "abc@domain.com"
        assert valid_email.username == "abc"
        assert valid_email.domain == "domain.com"
        assert valid_email.validated

    def test_equality(self):
        """Test EmailAddress eq method."""
        email_1 = EmailAddress("abc@domain.com")
        email_2 = EmailAddress("abc@domain.com")
        email_3 = EmailAddress("cba@domain.com")
        assert email_1 == email_2
        assert email_1 != email_3

    def test_gt_lt(self):
        """Test EmailAddress gt and lt methods."""
        email_1 = EmailAddress("abc@domain.com")
        email_2 = EmailAddress("bac@domain.com")
        email_3 = EmailAddress("cba@domain.com")
        assert email_1 < email_2
        assert email_2 < email_3
        assert email_3 > email_1

    def test_validate_valid_email(self):
        """Test EmailAddress _validate method."""
        email = EmailAddress("abc@domain.com")
        assert email._validate()

    def test_validate_no_at(self):
        """
        Test if initializing EmailAddress object without
        "@" results in object not being validated.
        """
        email = EmailAddress("abcdomain.com")
        assert not email._validate()

    def test_validate_double_at(self):
        """
        Test if initializing EmailAddress object with
        doubled "@" results in object not being validated.
        """
        email = EmailAddress("abc@@domain.com")
        assert not email._validate()

    def test_validate_before_at_less_than_one(self):
        """
        Test if initializing EmailAddress object without
        at least 1 character before "@" results in object
        not being validated.
        """
        email = EmailAddress("@domain.com")
        assert not email._validate()

    def test_validate_domain_between_at_and_dot_less_than_one(self):
        """
        Test if initializing EmailAddress object without
        at least 1 character between "@" and "." results
        in object not being validated.
        """
        email = EmailAddress("abc@.com")
        assert not email._validate()

    def test_validate_domain_after_dot_more_than_four(self):
        """
        Test if initializing EmailAddress object with
        more than 4 characters after the last "." results
        in object not being validated.
        """
        email = EmailAddress("abc@domain.comcom")
        assert not email._validate()

    def test_validate_domain_after_dot_less_than_one(self):
        """
        Test if initializing EmailAddress object with
        less than 1 character after the last "." results
        in object not being validated.
        """
        email = EmailAddress("abc@domain.")
        assert not email._validate()
