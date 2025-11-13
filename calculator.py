# https://github.com/renwen-lu/lab11-LR-WR
# Partner 1: Renwen Lu
# Partner 2: Ruijin Wang
import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def log(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Invalid input for logarithm")
    return math.log(b, a)

def exp(a, b):
    return a ** b
