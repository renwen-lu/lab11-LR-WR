# https://github.com/renwen-lu/lab11-LR-WR
# Partner 1: Renwen Lu
# Partner 2: Ruijin Wang

import unittest
import math
from calculator import *

class TestCalculatorPartner1(unittest.TestCase):
    def test_multiply(self):  
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 7), 0)

    def test_divide(self):  
        self.assertEqual(div(10, 2), 5)
        self.assertAlmostEqual(div(7, 2), 3.5)
        try:
            div(5, 0)
            self.fail("Expected ZeroDivisionError not raised")
        except ZeroDivisionError:
            pass

    def test_log_invalid_argument(self):
        try:
            logarithm(-2, 8)
            self.fail("Expected ValueError not raised")
        except ValueError:
            pass

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(1.5, 2.0), math.hypot(1.5, 2.0))

        def test_sqrt(self):
        try:
            square_root(-1)
            self.fail("Expected ValueError not raised")
        except ValueError:
            pass
        self.assertEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(2.25), 1.5)

    def test_add(self): 
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 4), 3)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self): 
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 7), -7)
        self.assertEqual(subtract(-2, -3), 1)

    def test_divide_by_zero(self):
        try:
            div(5, 0)
            self.fail("Expected ZeroDivisionError not raised")
        except ZeroDivisionError:
            pass

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(2, 8), 3)

def test_log_invalid_base(self):
        try:
            logarithm(-2, 8)
            self.fail("Expected ValueError not raised")
        except ValueError:
            pass

        try:
            logarithm(2, -8)
            self.fail("Expected ValueError not raised")
        except ValueError:
            pass

        try:
            logarithm(0, 10)
            self.fail("Expected ValueError not raised")
        except ValueError:
            pass



if __name__ == "__main__":
    unittest.main()


