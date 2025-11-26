# Assert that if the matrix is empty or has no rows/columns, the result is 0
assert len(matrix) == 0 or len(matrix[0]) == 0, "Matrix should be empty."
if len(matrix) == 0 or len(matrix[0]) == 0:
    assert res == 0, "Expected result must be 0 for empty matrix."

# Compute all submatrix sums and assert that res is the maximum found
max_sum = 0
for start_row in range(len(matrix)):
    for end_row in range(start_row, len(matrix)):
        for start_col in range(len(matrix[0])):
            for end_col in range(start_col, len(matrix[0])):
                submatrix_sum = sum(matrix[row][col] for row in range(start_row, end_row + 1) for col in range(start_col, end_col + 1))
                max_sum = max(max_sum, submatrix_sum)

# Assert that the result is the maximum submatrix sum or 0 if all numbers are negative
if max_sum <= 0:
    assert res == 0, "If the maximum submatrix sum is negative or zero, result should be 0."
else:
    assert res == max_sum, "Result should equal the maximum submatrix sum found."

# Assert that res is non-negative
assert res >= 0, "The result must be non-negative."