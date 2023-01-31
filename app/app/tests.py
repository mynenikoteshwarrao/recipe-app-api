"""
sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """test the calc module"""

    def test_add_numbers(self):
        """ test adding numbers together"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_substract_numbers(self):
        """ test adding numbers together"""
        res = calc.substract(5, 6)
        self.assertEqual(res, -1)
