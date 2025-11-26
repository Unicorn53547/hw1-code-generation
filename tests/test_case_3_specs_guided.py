import pytest
from solutions.mbpp.case_3_baseline import last_Digit_Factorial_Product

def test_empty_list():
    numbers = []
    assert last_Digit_Factorial_Product(numbers) == 1

def test_all_zeros():
    numbers = [0, 0, 0]
    assert last_Digit_Factorial_Product(numbers) == 1  # 0! = 1, product = 1

def test_all_ones():
    numbers = [1, 1, 1]
    assert last_Digit_Factorial_Product(numbers) == 1  # 1! = 1, product = 1

def test_mixture_small_values():
    numbers = [0, 1, 2, 3]
    assert last_Digit_Factorial_Product(numbers) == 6  # 0! * 1! * 2! * 3! = 1 * 1 * 2 * 6 = 12

def test_mixture_large_values():
    numbers = [4, 5]
    assert last_Digit_Factorial_Product(numbers) == 0  # 4! * 5! = 24 * 120 = 2880

def test_single_large_value():
    numbers = [10]
    assert last_Digit_Factorial_Product(numbers) == 0  # 10! ends in multiple zeros

def test_large_mixture():
    numbers = [6, 7, 8]
    assert last_Digit_Factorial_Product(numbers) == 0  # 6!, 7!, 8! all have trailing zeros

def test_large_values_with_zeros():
    numbers = [0, 10, 5]
    assert last_Digit_Factorial_Product(numbers) == 0  # 0! * 10! * 5! = 1 * (10! ends in zeros)

def test_single_zero():
    numbers = [0]
    assert last_Digit_Factorial_Product(numbers) == 1  # 0! = 1

def test_single_one():
    numbers = [1]
    assert last_Digit_Factorial_Product(numbers) == 1  # 1! = 1