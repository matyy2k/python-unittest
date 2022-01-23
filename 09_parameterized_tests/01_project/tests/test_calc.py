import unittest
from calculator.calc_math import SimpleClassCalculator


class TestSimpleClassCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleClassCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(-3, -2), -5)
        self.assertEqual(self.calc.add(-3, 2), -1)
        self.assertEqual(self.calc.add(3, -2), -1)
        self.assertEqual(self.calc.add(3, 2), -5)