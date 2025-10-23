# Write a function that takes in a string and character, replaces blank spaces in the string with the character, and returns the string.
def replace_blank(str1, char):
    # Use the replace method to replace all blank spaces with the given character
    return str1.replace(' ', char)

# Write a function that takes in a list of strings and a character. The function should replace all blank spaces in each string with the given character, and then concatenate all the modified strings into a single string. Finally, return the concatenated string.
def replace_and_concatenate(str_list, char):
    # Initialize an empty string to store the concatenated result
    result = ''
    # Iterate over each string in the list
    for str1 in str_list:
        # Replace all blank spaces in the string with the given character
        modified_str = replace_blank(str1, char)
        # Concatenate the modified string to the result
        result += modified_str
    # Return the concatenated result
    return result

assert replace_and_concatenate(['hello world', 'goodbye space'], '-') == 'hello-worldgoodbye-space'
assert replace_and_concatenate(['no spaces here'], '*') == 'no*spaces*here'
assert replace_and_concatenate(['', 'empty string'], '_') == 'empty_string'