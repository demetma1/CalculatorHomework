import math

class Calculator:
    result = 0

    def __init__(self):
        x = 4 - 2
        self.result = x;
        pass

    def add(self, a, b):
        c = a + b
        return c

    def subtract(self, a, b):
        c = b - a
        return c

    def multiply(self, a, b):
        c = a * b
        return c

    def divide(self, a, b):
        c = b / a
        return c

    def square(self, a):
        b = a * a
        return b

    def squareroot(self, a):
        b = math.sqrt(a)
        return b
