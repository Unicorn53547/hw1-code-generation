# Write a python function to find the last digit in factorial of a given number.
def last_Digit_Factorial(n):
    """
    This function calculates the last digit of the factorial of a given number.
    
    Args:
        n (int): The input number.
    
    Returns:
        int: The last digit of the factorial of the input number.
    """
    # Initialize the result variable to 1
    result = 1
    
    # Calculate the factorial of the input number
    for i in range(1, n + 1):
        result = (result * i) % 10
    
    # Return the last digit of the factorial
    return result

# Given a list of numbers, write a Python function to find the last digit of the product of the factorials of each number in the list.
def last_Digit_Factorial_Product(numbers):
    """
    This function calculates the last digit of the product of the factorials of each number in the given list.
    
    Args:
        numbers (list): A list of numbers.
    
    Returns:
        int: The last digit of the product of the factorials of each number in the list.
    """
    # Initialize the result variable to 1
    result = 1
    
    # Iterate over each number in the list
    for num in numbers:
        # Calculate the last digit of the factorial of the current number
        last_digit = last_Digit_Factorial(num)
        
        # Update the result by multiplying it with the last digit
        result = (result * last_digit) % 10
    
    # Return the last digit of the product
    return result

assert last_Digit_Factorial_Product([0, 1, 2, 3, 4]) == 8
assert last_Digit_Factorial_Product([5, 6, 7, 8, 9]) == 0
assert last_Digit_Factorial_Product([10, 11, 12, 13, 14]) == 0
assert last_Digit_Factorial_Product([15, 16, 17, 18, 19]) == 0
assert last_Digit_Factorial_Product([20, 21, 22, 23, 24]) == 0