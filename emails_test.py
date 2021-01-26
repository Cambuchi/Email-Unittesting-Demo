#!/usr/bin/env python3

# emails_test.py - implementing unittest to check emails.py.
# Made to satisfy Week 5 Qwiklabs assessment in the coursera course "Using Python to Interact with the
# Operating System" for Google's IT Automation with Python Professional Certificate.

import unittest
from emails import find_email


class EmailsTest(unittest.TestCase):
    def test_basic(self):
        testcase = [None, "Bree", "Campbell"]
        expected = "breee@abc.edu"
        self.assertEqual(find_email(testcase), expected)

    def test_one_name(self):
        testcase = [None, "John"]
        expected = "Missing parameters"
        self.assertEqual(find_email(testcase), expected)

    def test_two_name(self):
        testcase = [None, "Roy", "Cooper"]
        expected = "No email address found"
        self.assertEqual(find_email(testcase), expected)


if __name__ == '__main__':
    unittest.main()
