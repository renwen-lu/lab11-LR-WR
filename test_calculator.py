https://github.com/renwen-lu/lab11-LR-WR
Partner 1: Renwen Lu
Partner 2: Ruijin Wang

import unittest
import math

from calculator import *

class TestCalculatorPartner1(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 7), 0)

    def test_divide(self):
  
        self.assertEqual(div(2, 10), 5) 
        self.assertAlmostEqual(div(2, 7), 3.5)
       
 
    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)

    def test_sqrt(self):
        self.assertEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(2.25), 1.5)
        with self.assertRaises(ValueError):
            square_root(-1)


class TestCalculatorPartner2(unittest.TestCase):
   
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 4), 3)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 7), -7)
        self.assertEqual(subtract(-2, -3), 1)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5) # a=0, b=5

    def test_logarithm(self):
        self.assertAlmostEqual(log(10, 100), 2) 
        self.assertAlmostEqual(log(2, 8), 3)  

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(1, 10) 
        with self.assertRaises(ValueError):
            log(-2, 8)  
        with self.assertRaises(ValueError):
            log(10, -1) 


if __name__ == "__main__":
    unittest.main()
