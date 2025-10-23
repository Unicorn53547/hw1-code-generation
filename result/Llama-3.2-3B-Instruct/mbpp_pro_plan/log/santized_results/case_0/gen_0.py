# Write a function to replace all spaces in the given string with '%20'.
def replace_spaces(string):
    # Create a new string with spaces replaced
    new_string = string.replace(' ', '%20')
    return new_string

# Given a list of strings, replace all spaces in each string with '%20' and then concatenate all the modified strings into a single string. Finally, split the concatenated string by '%20' and return the resulting list of substrings.
def process_strings(string_list):
    # Initialize an empty string to store the concatenated string
    concatenated_string = ''
    
    # Iterate over each string in the list
    for string in string_list:
        # Replace spaces in the current string and concatenate it to the result string
        concatenated_string += replace_spaces(string) + ' '
    
    # Remove the trailing space and split the concatenated string by '%20'
    result = concatenated_string.strip().split('%20')
    
    # Return the resulting list of substrings
    return result

assert process_strings(['hello world', 'goodbye space']) == ['hello', 'worldgoodbye', 'space']
assert process_strings(['no_spaces', 'here']) == ['no_spaceshere']
assert process_strings(['multiple spaces   here']) == ['multiple', 'spaces', '', '', 'here']