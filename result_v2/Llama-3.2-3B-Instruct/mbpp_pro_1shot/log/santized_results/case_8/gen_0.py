# Write a function to convert a string to a list of strings split on the space character.
def string_to_list(string):
    """
    This function takes a string as input and returns a list of strings where each string is a word from the original string, split on the space character.

    Args:
        string (str): The input string to be converted.

    Returns:
        list: A list of strings where each string is a word from the original string.
    """
    # Split the input string into a list of words using the space character as the delimiter
    return string.split()

# Write a function to convert a list of strings into a list of lists where each sublist contains the words of the corresponding string from the original list, split on the space character.
def list_of_strings_to_list_of_lists(list_of_strings):
    """
    This function takes a list of strings as input and returns a list of lists where each sublist contains the words of the corresponding string from the original list.

    Args:
        list_of_strings (list): A list of strings where each string is a word from the original string.

    Returns:
        list: A list of lists where each sublist contains the words of the corresponding string from the original list.
    """
    # Initialize an empty list to store the result
    result = []
    # Iterate over each string in the input list
    for string in list_of_strings:
        # Split the current string into a list of words using the space character as the delimiter
        # and append the result to the main list
        result.append(string.split())
    # Return the final result
    return result

assert list_of_strings_to_list_of_lists(['hello world', 'python is fun']) == [['hello', 'world'], ['python', 'is', 'fun']]
assert list_of_strings_to_list_of_lists(['']) == [['']]
assert list_of_strings_to_list_of_lists(['singleword']) == [['singleword']]