# Write a function that takes in a string and character, replaces blank spaces in the string with the character, and returns the string.
def replace_blank(str1, char):
    # Plan:
    # 1. Use the replace() method of the string to replace all occurrences of ' ' (space) with the given character.
    # 2. Return the modified string.
    # 3. Handle edge cases where the input string is empty or contains only spaces.

    # Code:
    return str1.replace(' ', char)

assert replace_and_concatenate(['hello world', 'goodbye space'], '-') == 'hello-worldgoodbye-space'
assert replace_and_concatenate(['no spaces here'], '*') == 'no*spaces*here'
assert replace_and_concatenate(['', 'empty string'], '_') == 'empty_string'