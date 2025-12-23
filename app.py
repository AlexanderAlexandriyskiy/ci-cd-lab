""" Намеренная ошибка для демонстрации Ruff"""
from math import *

def add_numbers(a, b):
    """Сложение двух чисел."""
    return a + b

def multiply_numbers(x, y):
    """Умножение двух чисел."""
    result = x * y
    return result

if __name__ == "__main__":
    print("CI/CD лабораторная работа")
    print(f"2 + 3 = {add_numbers(2, 3)}")
