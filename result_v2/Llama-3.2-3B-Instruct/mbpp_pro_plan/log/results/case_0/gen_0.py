# Write a function to replace all spaces in the given string with '%20'.
def replace_spaces(string):
    # Create a new string with all spaces replaced with '%20'
    return string.replace(' ', '%20')

# Given a list of strings, replace all spaces in each string with '%20' and then concatenate all the modified strings into a single string. Finally, split the concatenated string by '%20' and return the resulting list of substrings.
def process_strings(string_list):
    # Initialize an empty string to store the concatenated modified strings
    concatenated_string = ''
    
    # Iterate over each string in the list
    for string in string_list:
        # Replace all spaces in the current string with '%20' and concatenate it to the result string
        concatenated_string += replace_spaces(string)
    
    # Split the concatenated string by '%20' and return the resulting list of substrings
    return concatenated_string.split('%20')

# Test the functions
print(replace_spaces('Hello World'))  # Expected output: 'Hello%20World'
print(process_strings(['Hello', 'World', 'Python']))  # Expected output: ['Hello%20World', 'Python']

assert process_strings(['hello world', 'goodbye space']) == ['hello', 'worldgoodbye', 'space']
assert process_strings(['no_spaces', 'here']) == ['no_spaceshere']
assert process_strings(['multiple spaces   here']) == ['multiple', 'spaces', '', '', 'here']