# Write a python function to find the last digit in factorial of a given number.
def last_Digit_Factorial(n):
    """
    This function calculates the last digit of the factorial of a given number.
    
    Args:
        n (int): The input number.
    
    Returns:
        int: The last digit of the factorial of the input number.
    """
    if n == 0:
        return 1
    elif n <= 2:
        return n
    elif n == 3:
        return 6
    elif n == 4:
        return 4
    else:
        return 0

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