# Write a function that takes in a string and character, replaces blank spaces in the string with the character, and returns the string.
def replace_blank(str1, char):
    return str1.replace(' ', char)

# Write a function that takes in a list of strings and a character. The function should replace all blank spaces in each string with the given character, and then concatenate all the modified strings into a single string. Finally, return the concatenated string.
def replace_and_concatenate(str_list, char):
    # Use a list comprehension to apply the replace_blank function to each string in the list
    modified_strings = [replace_blank(s, char) for s in str_list]
    # Concatenate all the modified strings into a single string
    concatenated_string = ''.join(modified_strings)
    return concatenated_string

# Test the functions with the provided test case
assert replace_and_concatenate(['hello world', 'goodbye space'], '-') == 'hello-worldgoodbye-space'

assert replace_and_concatenate(['hello world', 'goodbye space'], '-') == 'hello-worldgoodbye-space'
assert replace_and_concatenate(['no spaces here'], '*') == 'no*spaces*here'
assert replace_and_concatenate(['', 'empty string'], '_') == 'empty_string'