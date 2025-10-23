# Write a function to find the number of ways to partition a set of Bell numbers.
def bell_number(n):
    # Base case: B(0) = 1
    if n == 0:
        return 1
    # Recursive case: B(n) = Σ(B(k-1) * C(n-1, k-1)) for k = 1 to n
    else:
        total = 0
        for k in range(1, n+1):
            total += math.comb(n-1, k-1) * bell_number(k-1)
        return total

# Given a list of integers representing the sizes of sets, write a function to find the total number of ways to partition all these sets combined.
def total_bell_numbers(sizes):
    # Initialize the total number of ways to 1
    total_ways = 1
    # For each set size, multiply the total number of ways by the number of ways to partition that set
    for size in sizes:
        total_ways *= bell_number(size)
    return total_ways

assert total_bell_numbers([1, 2, 3]) == 8
assert total_bell_numbers([0, 1, 2]) == 4
assert total_bell_numbers([5, 5, 5]) == 156
assert total_bell_numbers([10]) == 115975
assert total_bell_numbers([0, 0, 0]) == 3