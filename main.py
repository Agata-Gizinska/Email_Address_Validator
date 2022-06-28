"""
This module provides the argument parser which allows
the user to perform implemented actions.
"""

import os
import argparse
from file_parser import EmailFileParser
from email_parser import EmailParser


def show_incorrect_emails(e_parser):
    """A function for executing "--incorrect-emails" command."""
    incorrect_emails = e_parser.show_incorrect_emails()
    print(f"Invalid emails ({len(incorrect_emails)}):")
    for email in incorrect_emails:
        print(f"\t {email}".expandtabs(4))


def search_emails_by_text(e_parser, searched_text):
    """A function for executing "--search <string>" command."""
    matches = e_parser.search_emails_by_text(text=searched_text)
    print(f"Found emails with '{searched_text}' in email ({len(matches)}):")
    for match in matches:
        print(f"\t {match}".expandtabs(4))


def group_emails_by_domain(e_parser):
    """A function for executing "--group-by-domain" command."""
    email_dict = e_parser.group_emails_by_domain()
    for key, values in email_dict.items():
        print(f"Domain {key} ({len(email_dict[key])}):")
        for value in values:
            print(f"\t {value}".expandtabs(4))


def find_emails_not_in_logs(e_parser, path):
    """A function for executing "--find-emails-not-in-logs <path>" command."""
    emails = e_parser.find_emails_not_in_logs(path)
    print(f"Emails not sent ({len(emails)}):")
    for email in emails:
        print(f"\t {email}".expandtabs(4))


def main(argv):
    """The main function containing logic for the argument parser."""
    parser = argparse.ArgumentParser()
    parser.add_argument("emailsdir", action="store", nargs="?",
                        default=os.path.dirname(os.path.abspath("main.py")),
                        metavar="<path_to_dir_with_email_files>",
                        help="Provide a path to the directory contining email \
                            addresses. Defaults to main.py directory")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-ic", "--incorrect-emails", action="store_true",
                       help="Print the number of invalid emails, \
                           then one invalid email per line")
    group.add_argument("-s", "--search", action="store", type=str,
                       metavar="<string>",
                       help="Take a string argument and print the number of \
                           found emails, then one found email per line")
    group.add_argument("-gbd", "--group-by-domain", action="store_true",
                       help="Group emails by one domain and order domains and \
                           emails alphabetically")
    group.add_argument("-feil", "--find-emails-not-in-logs", action="store",
                       metavar="<path_to_logs_file>",
                       help="Find emails that are not in the provided logs \
                           file. Print the numbers of found emails, then one \
                               found email per line sorted alphabetically.")
    args = parser.parse_args(argv)

    file_parser = EmailFileParser(args.emailsdir)
    email_parser = EmailParser(file_parser.valid_emails,
                               file_parser.invalid_emails)

    if args.incorrect_emails:
        show_incorrect_emails(email_parser)
    elif args.search:
        search_emails_by_text(email_parser, args.search)
    elif args.group_by_domain:
        group_emails_by_domain(email_parser)
    elif args.find_emails_not_in_logs:
        find_emails_not_in_logs(email_parser, args.find_emails_not_in_logs)


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
