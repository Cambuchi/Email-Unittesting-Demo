#!/usr/bin/env python3

# emails.py - script to check a csv of full names and related emails and returns the email from a given name.
# Made to satisfy Week 5 Qwiklabs assessment in the coursera course "Using Python to Interact with the
# Operating System" for Google's IT Automation with Python Professional Certificate.

import csv
import sys


def populate_dictionary(filename):
    """Populate a dictionary with name/email pairs for easy lookup."""
    email_dict = {}
    with open(filename) as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            name = str(row[0].lower())
            email_dict[name] = row[1]
    return email_dict


def find_email(argv):
    """ Return an email address based on the username given."""
    # Create the username based on the command line input.
    try:
        fullname = str(argv[1] + " " + argv[2])
        # Preprocess the data
        email_dict = populate_dictionary('/home/{{ username }}/data/user_emails.csv')
        # If email exists, print it
        if email_dict.get(fullname.lower()):
            return email_dict.get(fullname.lower())
        else:
            return "No email address found"
    except IndexError:
        return "Missing parameters"


def main():
    print(find_email(sys.argv))


if __name__ == "__main__":
    main()
