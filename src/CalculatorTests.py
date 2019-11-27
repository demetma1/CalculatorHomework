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
if __name__ == '__main__':
    unittest.main()

    def test_subtract_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(2, 4), 2)
        data = CsvReader('src/Unit Test Subtraction.csv').data
        for row in data:
            a = int(row['Value 1'])
            b = int(row['Value 2'])
            c = int(row['Result'])
            self.assertEqual(calculator.subtract(b, a), c)
if __name__ == '__main__':
    unittest.main()
