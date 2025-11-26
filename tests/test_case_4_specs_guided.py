import pytest
from solutions.mbpp.case_4_baseline import max_submatrix_sum

# def test_empty_matrix():
#     matrix = []
#     assert max_submatrix_sum(matrix) == 0

# def test_no_rows():
#     matrix = [[]]
#     assert max_submatrix_sum(matrix) == 0

def test_all_negative():
    max_submatrix_sum([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]) == 0

def test_all_zero():
    matrix = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert max_submatrix_sum(matrix) == 0

def test_all_positive():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert max_submatrix_sum(matrix) == 45

def test_mixed_values():
    assert max_submatrix_sum([[1, -2, 3], [4, 5, -6], [-7, 8, 9]]) == 17

def test_single_row():
    matrix = [
        [1, 2, -3, 4]
    ]
    assert max_submatrix_sum(matrix) == 6  # Submatrix: [1, 2, 4]

def test_single_column():
    matrix = [
        [1],
        [-2],
        [3]
    ]
    assert max_submatrix_sum(matrix) == 3  # Submatrix: [3]

def test_larger_matrix_mixed():
    matrix = [
        [1, -2, -1, 4],
        [-8, 4, 5, 7],
        [6, -3, 9, 2]
    ]
    assert max_submatrix_sum(matrix) == 27  # Submatrix: [[4, 5, 7], [6, -3, 9]]

def test_larger_matrix_all_negative_zero():
    matrix = [
        [-1, -2, -3],
        [-4, -5, -6],
        [-7, -8, -9]
    ]
    assert max_submatrix_sum(matrix) == 0