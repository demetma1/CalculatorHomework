import unittest
from Calculator import Calculator
from CsvReader import CsvReader

class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_results_property_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.result, 2)

    def test_add_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(2, 2), 4)
        data = CsvReader('src/Unit Test Addition.csv').data
        for row in data:
            a = int(row['Value 1'])
            b = int(row['Value 2'])
            c = int(row['Result'])
            self.assertEqual(calculator.add(a, b), c)

    def test_subtract_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(2, 4), 2)
        data = CsvReader('src/Unit Test Subtraction.csv').data
        for row in data:
            a = int(row['Value 1'])
            b = int(row['Value 2'])
            c = int(row['Result'])
            self.assertEqual(calculator.subtract(b, a), c)

    def test_multiply_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.multiply(2, 2), 4)
        data = CsvReader('src/Unit Test Multiplication.csv').data
        for row in data:
            a = int(row['Value 1'])
            b = int(row['Value 2'])
            c = int(row['Result'])
            self.assertEqual(calculator.multiply(b, a), c)

    def test_divide_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.divide(2, 4), 2)
        data = CsvReader('src/Unit Test Division.csv').data
        for row in data:
            a = int(row['Value 1'])
            b = int(row['Value 2'])
            c = int(row['Result'])
            self.assertEqual(calculator.divide(b, a), c)

    def test_square_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.square(2), 4)
        data = CsvReader('src/Unit Test Square.csv').data
        for row in data:
            a = int(row['Value 1'])
            b = int(row['Result'])
            self.assertEqual(calculator.square(a), b)

if __name__ == '__main__':
    unittest.main()

