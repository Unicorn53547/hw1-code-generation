# Write a function to convert a string to a list of strings split on the space character.
def string_to_list(string):
    """
    This function takes a string as input and returns a list of strings where each string is a word from the original string, split on the space character.

    Args:
        string (str): The input string to be converted.

    Returns:
        list: A list of strings where each string is a word from the original string.
    """
    # Plan:
    # 1. Split the input string into a list of words using the split() method.
    # 2. Return the list of words.

    # Code:
    return string.split()

# Write a function to convert a list of strings into a list of lists where each sublist contains the words of the corresponding string from the original list, split on the space character.
def list_of_strings_to_list_of_lists(list_of_strings):
    """
    This function takes a list of strings as input and returns a list of lists where each sublist contains the words of the corresponding string from the original list.

    Args:
        list_of_strings (list): The input list of strings to be converted.

    Returns:
        list: A list of lists where each sublist contains the words of the corresponding string from the original list.
    """
    # Plan:
    # 1. Initialize an empty list to store the result.
    # 2. Iterate over each string in the input list.
    # 3. For each string, split it into a list of words using the split() method.
    # 4. Append the list of words to the result list.

    # Code:
    result = []
    for string in list_of_strings:
        result.append(string.split())
    return result

assert list_of_strings_to_list_of_lists(['hello world', 'python is fun']) == [['hello', 'world'], ['python', 'is', 'fun']]
assert list_of_strings_to_list_of_lists(['']) == [['']]
assert list_of_strings_to_list_of_lists(['singleword']) == [['singleword']]