import pytest

from solutions.mbpp.case_4_baseline import (
    max_sub_array_sum,
    max_submatrix_sum,
)


def test_max_submatrix_sum_benchmark_cases():
    """
    Baseline tests: these are the benchmark-style asserts
    for the 2D max submatrix sum problem.
    """
    assert max_submatrix_sum([[1, 2, -1], [-3, 4, 5], [6, -7, 8]]) == 15
    assert max_submatrix_sum([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]) == 0
