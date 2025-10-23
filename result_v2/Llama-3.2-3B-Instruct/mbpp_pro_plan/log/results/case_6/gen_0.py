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
    # Create a copy of the input string to avoid modifying the original string
    modified_str = str1
    
    # Replace all blank spaces in the string with the specified character
    modified_str = modified_str.replace(" ", char)
    
    # Return the modified string
    return modified_str

# Write a function that takes in a list of strings and a character. The function should replace all blank spaces in each string with the given character, and then concatenate all the modified strings into a single string. Finally, return the concatenated string.
def replace_and_concatenate(str_list, char):
    """
    Replaces all blank spaces in each string in a list with a specified character and returns the concatenated string.

    Args:
        str_list (list): A list of strings.
        char (str): The character to replace blank spaces with.

    Returns:
        str: The concatenated string with blank spaces replaced.
    """
    # Initialize an empty string to store the concatenated result
    result = ""
    
    # Iterate over each string in the input list
    for string in str_list:
        # Replace all blank spaces in the current string with the specified character
        modified_str = replace_blank(string, char)
        
        # Concatenate the modified string to the result
        result += modified_str
    
    # Return the concatenated string
    return result

assert replace_and_concatenate(['hello world', 'goodbye space'], '-') == 'hello-worldgoodbye-space'
assert replace_and_concatenate(['no spaces here'], '*') == 'no*spaces*here'
assert replace_and_concatenate(['', 'empty string'], '_') == 'empty_string'