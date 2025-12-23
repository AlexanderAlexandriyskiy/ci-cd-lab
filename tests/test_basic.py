import sys
import os

# Добавляем родительскую директорию в путь Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import add_numbers, multiply_numbers

def test_addition():
    """Тест сложения."""
    assert add_numbers(2, 2) == 4
    assert add_numbers(0, 5) == 5

def test_multiplication():
    """Тест умножения."""
    assert multiply_numbers(3, 4) == 12
    assert multiply_numbers(0, 10) == 0

def test_string():
    """Тест строк."""
    text = "hello"
    assert text.upper() == "HELLO"
    assert len(text) == 5

def test_list():
    """Тест списков."""
    numbers = [1, 2, 3]
    assert sum(numbers) == 6
    assert len(numbers) == 3

def test_always_passes():
    """Тест который всегда проходит."""
    assert True
