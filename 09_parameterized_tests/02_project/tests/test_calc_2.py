import unittest
from calculator.calc_math import SimpleClassCalculator


class TestSimpleClassCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleClassCalculator()

    def test_add(self):
        cases = [
            (-3, -2, -5),
            (-3, 2, -1),
            (3, -2, 0),
            (3, 2, 0)
        ]
        for x, y, result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(self.calc.add(x, y), result)