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
    # Use the replace() method to replace all occurrences of ' ' (space) with the given character
    return str1.replace(' ', char)

# Write a function that takes in a list of strings and a character. The function should replace all blank spaces in each string with the given character, and then concatenate all the modified strings into a single string. Finally, return the concatenated string.
def replace_and_concatenate(str_list, char):
    """
    Replaces all blank spaces in each string of a given list with a specified character, 
    and then concatenates all the modified strings into a single string.

    Args:
        str_list (list): A list of strings.
        char (str): The character to replace blank spaces with.

    Returns:
        str: The concatenated string with blank spaces replaced.
    """
    # Use a list comprehension to apply the replace_blank function to each string in the list
    modified_list = [replace_blank(s, char) for s in str_list]
    
    # Use the join() method to concatenate all the modified strings into a single string
    return ''.join(modified_list)

assert replace_and_concatenate(['hello world', 'goodbye space'], '-') == 'hello-worldgoodbye-space'
assert replace_and_concatenate(['no spaces here'], '*') == 'no*spaces*here'
assert replace_and_concatenate(['', 'empty string'], '_') == 'empty_string'