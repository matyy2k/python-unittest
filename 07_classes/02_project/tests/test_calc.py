import sys
import unittest


path = r'D:\$$\python-unittest\07_classes\02_project'
sys.path.append(path)

from calculator.calc_math import SimpleClassCalculator


class TestSimpleClassCalculator(unittest.TestCase):

    def test_add(self):
        calc = SimpleClassCalculator()
        self.assertEqual(calc.add(3, 4), 7)

    def test_sub(self):
        calc = SimpleClassCalculator()
        self.assertEqual(calc.sub(3, 4), -1)

    def test_mul(self):
        calc = SimpleClassCalculator()
        self.assertEqual(calc.mul(3, 4), 12)
