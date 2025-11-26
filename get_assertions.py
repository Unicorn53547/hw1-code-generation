# exercise3_part1_generate_specs.py
#
# Usage:
#   export OPENAI_API_KEY=...
#   python exercise3_part1_generate_specs.py
#
# This script sends two prompts (for Exercise 3 Part 1) to an LLM and saves the
# raw specification assertions to specs_raw/*.py for manual inspection.

from pathlib import Path

import os
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = ""   # <<< YOUR KEY HERE

client = OpenAI()

resp = client.responses.create(
    model="gpt-4o-mini",
    input="hello world"
)
print(resp.output_text)


# ---------- Prompts ----------

PROMPT_LAST_DIGIT_FACT_PRODUCT = """You are helping to write formal specifications for the following Python function:

def last_Digit_Factorial_Product(numbers: list[int]) -> int:
    \"\"\"
    Given a list of non-negative integers `numbers`, consider the factorial n! of each
    element n in the list. Compute the product of all these factorials and return the
    last decimal digit (0-9) of that product.

    If `numbers` is empty, the product is defined as 1, so the function returns 1.
    You may assume there is a helper function last_Digit_Factorial(n) that correctly
    returns the last digit of n!, but you must NOT call it in your specifications.
    \"\"\"

Let `numbers` denote the input list and `res` denote the expected return value of
last_Digit_Factorial_Product(numbers).

Write a set of Python `assert` statements that specify the correct relationship
between `numbers` and `res`.

Requirements:
- Do NOT call last_Digit_Factorial_Product or any factorial helper inside the
  assertions (no self-reference).
- Do NOT use any side-effecting operations such as:
  - modifying data structures in place (append, add, remove, sort, etc.)
  - performing I/O (print, input, file read/write)
  - using randomness or timing (random.random, time.time, datetime.now, etc.).
- You may use pure arithmetic, boolean logic, if-statements, loops, and pure
  builtins such as all(), any(), len(), range(), max(), min().

Assume all integers in `numbers` are >= 0.

Produce 5–8 assertions that capture important logical properties of the
relationship between `numbers` and `res`. Use only `numbers`, `res`, and local
variables you define in the assertions.

Return ONLY Python code, consisting of `assert` statements and any `if` blocks
needed, for example:

assert ...
if ...:
    assert ...
"""

PROMPT_MAX_SUBMATRIX_SUM = """You are helping to write formal specifications for the following Python function:

def max_submatrix_sum(matrix: list[list[int]]) -> int:
    \"\"\"
    Given a 2D list `matrix` of integers, return the sum of the largest contiguous
    submatrix. A submatrix is any rectangular block obtained by choosing a contiguous
    range of rows and a contiguous range of columns.

    If the matrix is empty or has no rows/columns, the function returns 0.
    If all entries are negative, we define the maximum submatrix sum to be 0
    (we allow choosing an empty submatrix with sum 0).
    \"\"\"

Let `matrix` denote the input and `res` denote the expected return value of
max_submatrix_sum(matrix).

Write a set of Python `assert` statements that specify the correct relationship
between `matrix` and `res`.

Requirements:
- Do NOT call max_submatrix_sum inside the assertions (no self-reference).
- Do NOT use any side-effecting operations such as:
  - modifying data structures in place (append, add, remove, sort, etc.)
  - performing I/O (print, input, file read/write)
  - using randomness or timing (random.random, time.time, datetime.now, etc.).
- You may use pure arithmetic, boolean logic, loops, and pure builtins such as
  all(), any(), len(), range(), max(), min(), sum().

Produce 5–8 assertions that capture important logical properties of the
relationship between `matrix` and `res`. Use only `matrix`, `res`, and local
variables you define in the assertions.

Return ONLY Python code, consisting of `assert` statements and any `if` blocks
needed, for example:

assert ...
if ...:
    assert ...
"""


def call_model(prompt: str) -> str:
    client = OpenAI()
    response = client.responses.create(
        model="gpt-4o-mini",  # or whatever model your course uses
        input=prompt,
        max_output_tokens=2048,
    )
    # responses API provides a convenience property:
    return response.output_text


def main():
    out_dir = Path("specs_raw")
    out_dir.mkdir(exist_ok=True)

    cases = {
        "case_3_last_Digit_Factorial_Product": PROMPT_LAST_DIGIT_FACT_PRODUCT,
        "case_4_max_submatrix_sum": PROMPT_MAX_SUBMATRIX_SUM,
    }

    for name, prompt in cases.items():
        print("=" * 80)
        print(f"Sending prompt for {name}...")
        text = call_model(prompt)
        print(f"Raw model output for {name}:\n")
        print(text)
        print()

        out_path = out_dir / f"{name}_specs_raw.py"
        out_path.write_text(text, encoding="utf-8")
        print(f"[saved specs to {out_path}]\n")


if __name__ == "__main__":
    main()
