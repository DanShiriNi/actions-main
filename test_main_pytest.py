import pytest
from main import calculate_average

# Тест для набора положительных чисел
def test_positive_numbers():
    assert calculate_average([1.0, 2.0, 3.0]) == pytest.approx(2)
    print("Tested by Shishelov Daniil!")

# Тест для набора отрицательных чисел
def test_negative_numbers():
    assert calculate_average([-1.0, -2.0, -3.0]) == pytest.approx(-2)
    print("Tested by Shishelov Daniil!")

# Тест для пустого списка
def test_empty_list():
    assert calculate_average([]) is None
    print("Tested by Shishelov Daniil!")