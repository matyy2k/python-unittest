import unittest
from calculator.calc_math import SimpleClassCalculator


def setUpModule():
    print('setting up...')
    global calc
    calc = SimpleClassCalculator()

def tearDownModule():
    print('tearing down...')
    global calc
    del calc


class TestSimpleClassCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(3, 4), 7)

    def test_sub(self):
        self.assertEqual(calc.sub(3, 4), -1)

    def test_mul(self):
        self.assertEqual(calc.mul(3, 4), 12)
