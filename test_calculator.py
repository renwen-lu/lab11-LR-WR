import unittest
from calculator import *

# https://github.com/renwen-lu/lab11-LR-WR
# Partner 1: Renwen Lu
# Partner 2: Ruijin Wang

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 7), 0)

    def test_divide(self):  # 3 assertions
        self.assertEqual(div(10, 2), 5)
        self.assertAlmostEqual(div(7, 2), 3.5)
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)
    # ##########################

    import unittest
    from calculator import *

    # https://github.com/renwen-lu/lab11-LR-WR
    # Partner 1: Renwen Lu
    # Partner 2: Ruijin Wang

    class TestCalculator(unittest.TestCase):
        ######### Partner 2
        def test_add(self):  # 3 assertions
            self.assertEqual(add(2, 3), 5)
            self.assertEqual(add(-1, 4), 3)
            self.assertEqual(add(0, 0), 0)

        def test_subtract(self):  # 3 assertions
            self.assertEqual(sub(5, 3), 2)
            self.assertEqual(sub(0, 7), -7)
            self.assertEqual(sub(-2, -3), 1)

        ##########################

        ######## Partner 1
        def test_multiply(self):  # 3 assertions
            self.assertEqual(mul(3, 4), 12)
            self.assertEqual(mul(-2, 5), -10)
            self.assertEqual(mul(0, 7), 0)

        def test_divide(self):  # 3 assertions
            self.assertEqual(div(10, 2), 5)
            self.assertAlmostEqual(div(7, 2), 3.5)
            with self.assertRaises(ZeroDivisionError):
                div(5, 0)

        ##########################

        ######## Partner 2
        def test_divide_by_zero(self):  # 1 assertion
            with self.assertRaises(ZeroDivisionError):
                div(5, 0)

        def test_logarithm(self):  # 3 assertions
            self.assertEqual(log(10, 100), 2)
            self.assertAlmostEqual(log(2, 8), 3)
            self.assertAlmostEqual(log(3, 27), 3)

        def test_log_invalid_base(self):  # 1 assertion
            with self.assertRaises(ValueError):
                log(-2, 8)



        ######## Partner 1
        def test_log_invalid_argument(self):
            with self.assertRaises(ValueError):
                log(-2, 8)

        def test_hypotenuse(self):
            self.assertEqual(hypotenuse(3, 4), 5)
            self.assertEqual(hypotenuse(5, 12), 13)
            self.assertAlmostEqual(hypotenuse(1.5, 2.0), math.hypot(1.5, 2.0))

        def test_sqrt(self):
            self.assertEqual(square_root(9), 3)
            self.assertAlmostEqual(square_root(2.25), 1.5)
            with self.assertRaises(ValueError):
                square_root(-1)

    # Do not touch this
    if __name__ == "__main__":
        unittest.main()

