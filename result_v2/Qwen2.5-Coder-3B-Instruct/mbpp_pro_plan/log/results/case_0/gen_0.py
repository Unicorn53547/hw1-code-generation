# Write a function to replace all spaces in the given string with '%20'.
def replace_spaces(string):
    # Use the replace method to replace all spaces with '%20'
    return string.replace(' ', '%20')

# Given a list of strings, replace all spaces in each string with '%20' and then concatenate all the modified strings into a single string. Finally, split the concatenated string by '%20' and return the resulting list of substrings.
def process_strings(string_list):
    # Initialize an empty list to store the modified strings
    modified_strings = []
    
    # Iterate over each string in the string list
    for string in string_list:
        # Replace all spaces in the string with '%20'
        modified_string = replace_spaces(string)
        # Append the modified string to the list
        modified_strings.append(modified_string)
    
    # Concatenate all the modified strings into a single string
    concatenated_string = ''.join(modified_strings)
    
    # Split the concatenated string by '%20' and return the resulting list of substrings
    return concatenated_string.split('%20')

assert process_strings(['hello world', 'goodbye space']) == ['hello', 'worldgoodbye', 'space']
assert process_strings(['no_spaces', 'here']) == ['no_spaceshere']
assert process_strings(['multiple spaces   here']) == ['multiple', 'spaces', '', '', 'here']