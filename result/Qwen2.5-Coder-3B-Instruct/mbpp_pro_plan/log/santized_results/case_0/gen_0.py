# Write a function to replace all spaces in the given string with '%20'.
def replace_spaces(string):
    # Use the replace method to replace all spaces with '%20'
    return string.replace(' ', '%20')

# Given a list of strings, replace all spaces in each string with '%20' and then concatenate all the modified strings into a single string. Finally, split the concatenated string by '%20' and return the resulting list of substrings.
def process_strings(string_list):
    # Initialize an empty list to store the modified strings
    modified_strings = []
    
    # Iterate over each string in the list
    for string in string_list:
        # Replace spaces in the string and add it to the modified_strings list
        modified_strings.append(replace_spaces(string))
    
    # Concatenate all the modified strings into a single string
    concatenated_string = ''.join(modified_strings)
    
    # Split the concatenated string by '%20' and return the resulting list of substrings
    return concatenated_string.split('%20')

assert process_strings(['hello world', 'goodbye space']) == ['hello', 'worldgoodbye', 'space']
assert process_strings(['no_spaces', 'here']) == ['no_spaceshere']
assert process_strings(['multiple spaces   here']) == ['multiple', 'spaces', '', '', 'here']