import pytest

from solutions.mbpp.case_3_baseline import (
    last_Digit_Factorial,
    last_Digit_Factorial_Product,
)


def test_last_Digit_Factorial_Product_benchmark_cases():
    """
    Baseline tests: these are exactly the benchmark-style asserts
    from the MBPP-Pro problem for last_Digit_Factorial_Product.
    """
    assert last_Digit_Factorial_Product([5, 6, 7, 8, 9]) == 0


