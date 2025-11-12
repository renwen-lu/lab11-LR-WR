"""
calculator.py
# https://github.com/renwen-lu/lab11-LR-WR
# Partner 1: Renwen Lu
# Partner 2: Ruijin Wang
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y



