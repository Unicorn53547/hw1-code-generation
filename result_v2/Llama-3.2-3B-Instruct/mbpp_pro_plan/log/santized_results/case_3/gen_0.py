# Write a function to find the number of ways to partition a set of Bell numbers.
def bell_number(n):
    """
    Calculate the nth Bell number.

    The Bell numbers are a sequence of numbers that arise in combinatorial mathematics,
    and are named after the mathematician Eric Temple Bell.

    The Bell numbers are defined recursively as follows:
    B(0) = 1
    B(n) = Σ(B(k) * C(n-1, k)) for k = 1 to n

    where C(n, k) is the binomial coefficient, defined as:
    C(n, k) = n! / (k! * (n-k)!)

    :param n: The index of the Bell number to calculate
    :return: The nth Bell number
    """
    if n == 0:
        return 1
    else:
        bell_nums = [1]
        for i in range(1, n+1):
            bell_num = 0
            for k in range(1, i+1):
                bell_num += bell_nums[k-1] * math.comb(i-1, k-1)
            bell_nums.append(bell_num)
        return bell_nums[n]

# Given a list of integers representing the sizes of sets, write a function to find the total number of ways to partition all these sets combined.
def total_bell_numbers(sizes):
    """
    Calculate the total number of ways to partition a set of Bell numbers.

    :param sizes: A list of integers representing the sizes of sets
    :return: The total number of ways to partition all these sets combined
    """
    total_ways = 1
    for size in sizes:
        total_ways *= bell_number(size)
    return total_ways


assert total_bell_numbers([1, 2, 3]) == 8
assert total_bell_numbers([0, 1, 2]) == 4
assert total_bell_numbers([5, 5, 5]) == 156
assert total_bell_numbers([10]) == 115975
assert total_bell_numbers([0, 0, 0]) == 3