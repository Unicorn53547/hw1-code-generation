# Write a function to convert a string to a list of strings split on the space character.
def string_to_list(string):
    # Split the string by spaces and return the resulting list
    return string.split()

# Write a function to convert a list of strings into a list of lists where each sublist contains the words of the corresponding string from the original list, split on the space character.
def list_of_strings_to_list_of_lists(list_of_strings):
    # Use the string_to_list function to split each string in the list and store the results in a new list
    return [string_to_list(s) for s in list_of_strings]

assert list_of_strings_to_list_of_lists(['hello world', 'python is fun']) == [['hello', 'world'], ['python', 'is', 'fun']]
assert list_of_strings_to_list_of_lists(['']) == [['']]
assert list_of_strings_to_list_of_lists(['singleword']) == [['singleword']]