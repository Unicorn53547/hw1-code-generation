# Write a function to replace all spaces in the given string with '%20'.
def replace_spaces(string):
    return string.replace(' ', '%20')

# Given a list of strings, replace all spaces in each string with '%20' and then concatenate all the modified strings into a single string. Finally, split the concatenated string by '%20' and return the resulting list of substrings.
def process_strings(string_list):
    # Replace all spaces in each string with '%20' and store the modified strings in a list
    modified_strings = [s.replace(' ', '%20') for s in string_list]
    
    # Concatenate all the modified strings into a single string
    concatenated_string = ''.join(modified_strings)
    
    # Split the concatenated string by '%20' and return the resulting list of substrings
    return concatenated_string.split('%20')

assert process_strings(['hello world', 'goodbye space']) == ['hello', 'worldgoodbye', 'space']
assert process_strings(['no_spaces', 'here']) == ['no_spaceshere']
assert process_strings(['multiple spaces   here']) == ['multiple', 'spaces', '', '', 'here']