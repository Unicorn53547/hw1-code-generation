# Write a function to toggle the case of all characters in a string.
def toggle_string(string):
    # Initialize an empty list to store the toggled characters
    toggled_chars = []
    # Iterate over each character in the string
    for char in string:
        # Check if the character is uppercase
        if char.isupper():
            # Convert the character to lowercase and append to the list
            toggled_chars.append(char.lower())
        # Check if the character is lowercase
        elif char.islower():
            # Convert the character to uppercase and append to the list
            toggled_chars.append(char.upper())
        # If the character is neither uppercase nor lowercase, append it as is
        else:
            toggled_chars.append(char)
    # Join the list of toggled characters into a single string and return it
    return ''.join(toggled_chars)

# Given a list of strings, write a function to toggle the case of all characters in each string and then concatenate the results into a single string, with each toggled string separated by a space.
def toggle_and_concatenate(strings):
    # Initialize an empty list to store the toggled strings
    toggled_strings = []
    # Iterate over each string in the list
    for string in strings:
        # Toggle the case of all characters in the string using the toggle_string function
        toggled_string = toggle_string(string)
        # Append the toggled string to the list
        toggled_strings.append(toggled_string)
    # Join the list of toggled strings into a single string with each toggled string separated by a space and return it
    return ' '.join(toggled_strings)

assert toggle_and_concatenate(['Hello', 'World']) == 'hELLO wORLD'
assert toggle_and_concatenate(['Python', 'Programming']) == 'pYTHON pROGRAMMING'
assert toggle_and_concatenate(['aBcDeF']) == 'AbCdEf'
assert toggle_and_concatenate(['123', '456']) == '123 456'
assert toggle_and_concatenate([]) == ''