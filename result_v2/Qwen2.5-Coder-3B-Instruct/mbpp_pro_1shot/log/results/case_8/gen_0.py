# Write a function to convert a string to a list of strings split on the space character.
def string_to_list(string):
    return string.split()

# Write a function to convert a list of strings into a list of lists where each sublist contains the words of the corresponding string from the original list, split on the space character.
def list_of_strings_to_list_of_lists(list_of_strings):
    return [string_to_list(s) for s in list_of_strings]

# Test the functions
assert list_of_strings_to_list_of_lists(['hello world', 'python is fun']) == [['hello', 'world'], ['python', 'is', 'fun']]

assert list_of_strings_to_list_of_lists(['hello world', 'python is fun']) == [['hello', 'world'], ['python', 'is', 'fun']]
assert list_of_strings_to_list_of_lists(['']) == [['']]
assert list_of_strings_to_list_of_lists(['singleword']) == [['singleword']]