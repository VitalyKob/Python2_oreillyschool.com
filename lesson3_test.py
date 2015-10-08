"""Demonstrates the unittest module in action."""

import unittest

def title(s):
    "How close is this function to str.title()?"
    return s[0].upper()+s[1:]


class TestTitle(unittest.TestCase):

    def test_title(self):
        str = "new day"
        self.assertEqual(title(str), str.title(), "comparing function title with native method")
        

if __name__ == "__main__":
    unittest.main()
