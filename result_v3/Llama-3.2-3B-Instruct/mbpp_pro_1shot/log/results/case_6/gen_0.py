# Write a function that takes in a string and character, replaces blank spaces in the string with the character, and returns the string.
def replace_blank(str1, char):
    return str1.replace(' ', char)

# Write a function that takes in a list of strings and a character. The function should replace all blank spaces in each string with the given character, and then concatenate all the modified strings into a single string. Finally, return the concatenated string.
def replace_and_concatenate(str_list, char):
    # Use list comprehension to replace blank spaces in each string with the given character
    modified_list = [s.replace(' ', char) for s in str_list]
    # Use the join function to concatenate all the modified strings into a single string
    return ''.join(modified_list)

assert replace_and_concatenate(['hello world', 'goodbye space'], '-') == 'hello-worldgoodbye-space'
assert replace_and_concatenate(['no spaces here'], '*') == 'no*spaces*here'
assert replace_and_concatenate(['', 'empty string'], '_') == 'empty_string'