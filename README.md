# Email Address Validator

Welcome to my implementation of the Email Address Validator!

## General info

This program allows to perform some operations on the email data.

The program is based on argument parser which allows you to:

- Print the number of invalid emails, then one invalid email per line;

- Take a string argument and print the number of found emails, then one found
email per line;

- Group emails by one domain and order domains and emails alphabetically;

- Find emails that are not in the provided logs file. Print the numbers of
found emails, then one found email per line sorted alphabetically.

## Technology and Setup

- Python 3.10

To setup environment use pip:

```pip install -r requirements.txt```

## Usage

Using the terminal change the current directory to the directory with the 
main.py file. Run an appropriate command.

The program takes a path to the directory with email files as a positional
argument, defaults to the directory with ```main.py```. Therefore, you may
want to provide a string with an appropriate path.

Available commands:

```python main.py <path_to_dir_with_email_files> --incorrect-emails```
or ```python main.py <path_to_dir_with_email_files> -ic```

```python main.py <path_to_dir_with_email_files> --search <string>```
or ```python main.py <path_to_dir_with_email_files> -s <string>```

```python main.py <path_to_dir_with_email_files> --group-by-domain```
or ```python main.py <path_to_dir_with_email_files> -gbd```

```python main.py <path_to_dir_with_email_files> --find-emails-not-in-logs <path>```
or ```python main.py <path_to_dir_with_email_files> -feil <path>```

Use command ```python main.py --help``` to get help messages. 

You may also get help messages for each option, for example:

```python main.py --incorrect-emails --help```

### Example Usage

```python main.py ".\emails" --incorrect-emails```

```python main.py ".\emails" --search "agustin"```

```python main.py ".\emails" --group-by-domain```

```python main.py ".\emails" -feil ".\email-sent.logs"```
