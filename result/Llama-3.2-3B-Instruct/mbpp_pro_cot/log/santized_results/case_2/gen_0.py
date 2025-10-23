# Write a function to toggle the case of all characters in a string.
def toggle_string(string):
    """
    This function takes a string as input, toggles the case of all characters in the string, 
    and returns the resulting string.

    Args:
        string (str): The input string.

    Returns:
        str: The string with all characters toggled.
    """
    return string.swapcase()

assert toggle_and_concatenate(['Hello', 'World']) == 'hELLO wORLD'
assert toggle_and_concatenate(['Python', 'Programming']) == 'pYTHON pROGRAMMING'
assert toggle_and_concatenate(['aBcDeF']) == 'AbCdEf'
assert toggle_and_concatenate(['123', '456']) == '123 456'
assert toggle_and_concatenate([]) == ''