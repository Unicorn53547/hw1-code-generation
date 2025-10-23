# Write a function that takes in a string and character, replaces blank spaces in the string with the character, and returns the string.
def replace_blank(str1, char):
    """
    Replaces all blank spaces in a given string with a specified character.

    Args:
        str1 (str): The input string.
        char (str): The character to replace blank spaces with.

    Returns:
        str: The modified string with blank spaces replaced.
    """
    return str1.replace(" ", char)

assert replace_and_concatenate(['hello world', 'goodbye space'], '-') == 'hello-worldgoodbye-space'
assert replace_and_concatenate(['no spaces here'], '*') == 'no*spaces*here'
assert replace_and_concatenate(['', 'empty string'], '_') == 'empty_string'