import unittest
from main import calculate_average

class TestCalculateAverage(unittest.TestCase):
    # Тест для набора положительных чисел
    def test_positive_numbers(self):
        self.assertAlmostEqual(calculate_average([1.0, 2.0, 3.0]), 2)
        print("Tested by Shishelov Daniil!")
    
    # Тест для набора отрицательных чисел
    def test_negative_numbers(self):
        self.assertAlmostEqual(calculate_average([-1.0, -2.0, -3.0]), -2)
        print("Tested by Shishelov Daniil!")
    
    # Тест для пустого списка
    def test_empty_list(self):
        self.assertIsNone(calculate_average([]))
        print("Tested by Shishelov Daniil!")