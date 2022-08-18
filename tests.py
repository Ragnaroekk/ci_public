import unittest
from datetime import datetime
from task import my_datetime


class TestCase(unittest.TestCase):
    # test 0 seconds per canvas example
    def test8(self):
        seconds = 0
        self.assertEqual(my_datetime(seconds), "01-01-1970")

    # test 123456789 seconds per canvas example
    def test9(self):
        seconds = 123456789
        self.assertEqual(my_datetime(seconds), "11-29-1973")

    # test 9876543210 seconds per canvas example
    def test10(self):
        seconds = 9876543210
        self.assertEqual(my_datetime(seconds), "12-22-2282")

    # test 201653971200 seconds per canvas example
    def test11(self):
        seconds = 201653971200
        self.assertEqual(my_datetime(seconds), "02-29-8360")

    # check for year divisible by 400
    def test12(self):
        seconds = 190301442001

        months = datetime.utcfromtimestamp(seconds).month
        days = datetime.utcfromtimestamp(seconds).day
        years = datetime.utcfromtimestamp(seconds).year

        self.assertEqual(my_datetime(seconds), f"{months:02d}-{days:02d}-{years}")

    # check for a year divisible by 100 and not 400
    def test13(self):
        seconds = 95641256401

        months = datetime.utcfromtimestamp(seconds).month
        days = datetime.utcfromtimestamp(seconds).day
        years = datetime.utcfromtimestamp(seconds).year

        self.assertEqual(my_datetime(seconds), f"{months:02d}-{days:02d}-{years}")


if __name__ == '__main__':
    unittest.main()