# exercise3_part2_generate_tests.py
"""
Call an OpenAI model to generate spec-guided test cases
for Exercise 3, Part 2.

This script will write:
  - tests/test_case_3_specs_guided.py
  - tests/test_case_4_specs_guided.py
"""

from pathlib import Path
from openai import OpenAI
import os

# ===== 0. Configure your API key & model here =====
# Option A: hard-code the key (do NOT commit real keys to public repos)
os.environ["OPENAI_API_KEY"] = ""   # <<< YOUR KEY HERE

client = OpenAI()

MODEL_NAME = "gpt-4o-mini"  # or whatever model your course wants


# ===== 1. Prompts for each function =====

PROMPT_TESTS_LAST_DIGIT_FACT_PRODUCT = """You are helping to write tests for the following function:

from solutions.mbpp.case_3_baseline import last_Digit_Factorial_Product

def last_Digit_Factorial_Product(numbers: list[int]) -> int:
    \"\"\"
    Given a list of non-negative integers `numbers`, consider the factorial n! of each
    element n in the list. Compute the product of all these factorials and return the
    last decimal digit (0-9) of that product.
    \"\"\"

We have the following specification examples over `numbers` and the expected result `res`:

# Example 1: Testing with the empty list.
numbers = []
res = 1  # Expected result since product of an empty list is defined as 1
assert res == 1

Using these examples as a specification of the relationship between `numbers` and
the true result `res`, generate a set of pytest test functions that call
last_Digit_Factorial_Product and assert its correct behavior.

Requirements for the output:
- Output valid Python code that can be placed in a pytest file.
- At the top, import:
    import pytest
    from solutions.mbpp.case_3_baseline import last_Digit_Factorial_Product
- Define multiple test_... functions.
- Each test should call last_Digit_Factorial_Product(numbers) and compare its
  return value to the expected result implied by the examples (or simple reasoning
  consistent with them).
- Use a variety of inputs, including edge cases (empty list, all zeros, all ones,
  mixture of small and large values).
- DO NOT redefine last_Digit_Factorial_Product in the output.
- DO NOT print or read input; just use assert statements.

Return ONLY Python code consisting of imports (as specified) and pytest test functions.
"""


PROMPT_TESTS_MAX_SUBMATRIX_SUM = """You are helping to write tests for the following function:

from solutions.mbpp.case_4_baseline import max_submatrix_sum

def max_submatrix_sum(matrix: list[list[int]]) -> int:
    \"\"\"
    Given a 2D list `matrix` of integers, return the sum of the largest contiguous
    submatrix. A submatrix is any rectangular block obtained by choosing a contiguous
    range of rows and a contiguous range of columns.

    If the matrix is empty or has no rows/columns, the function returns 0.
    If all entries are negative, we define the maximum submatrix sum to be 0.
    \"\"\"

We have the following specification-style properties:

- If the matrix is empty or has no rows/columns, the result is 0.
- The result is the maximum sum over all possible contiguous submatrices.
- If all entries are negative or zero, the result should be 0.
- The result is always non-negative.

Using these properties as a specification of the correct behavior, generate pytest
tests that call max_submatrix_sum and check that it returns the correct value.

Requirements for the output:
- Output valid Python code that can be placed in a pytest file.
- At the top, import:
    import pytest
    from solutions.mbpp.case_4_baseline import max_submatrix_sum
- Define multiple test_... functions.
- Each test should call max_submatrix_sum(matrix) and compare its return value
  to the mathematically correct result (you can compute the correct result
  inline using explicit sums in small examples).
- Use a variety of matrices: empty, all negative, all positive, mixed, single row,
  single column, and larger sizes.
- DO NOT redefine max_submatrix_sum in the output.
- DO NOT print or read input; just use assert statements.

Return ONLY Python code consisting of imports (as specified) and pytest test functions.
"""


# ===== 2. Helper to call the model =====

def call_model(prompt: str) -> str:
    resp = client.responses.create(
        model=MODEL_NAME,
        input=prompt,
        max_output_tokens=1200,
    )
    # responses API has .output_text for the combined text
    return resp.output_text


# ===== 3. Main: generate two test files =====

def main():
    out_dir = Path("tests")
    out_dir.mkdir(exist_ok=True)

    cases = {
        "test_case_3_specs_guided.py": PROMPT_TESTS_LAST_DIGIT_FACT_PRODUCT,
        "test_case_4_specs_guided.py": PROMPT_TESTS_MAX_SUBMATRIX_SUM,
    }

    for filename, prompt in cases.items():
        print(f"Generating tests for {filename}...")
        code = call_model(prompt)
        out_path = out_dir / filename
        out_path.write_text(code, encoding="utf-8")
        print(f"  -> saved to {out_path}")


if __name__ == "__main__":
    main()
