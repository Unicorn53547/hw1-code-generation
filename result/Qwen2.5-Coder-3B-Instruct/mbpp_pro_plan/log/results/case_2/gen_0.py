# Write a function to toggle the case of all characters in a string.
def toggle_string(string):
    # Initialize an empty list to store the toggled characters
    toggled_chars = []
    # Iterate over each character in the string
    for char in string:
        # Check if the character is uppercase
        if char.isupper():
            # Convert to lowercase and append to the list
            toggled_chars.append(char.lower())
        else:
            # Convert to uppercase and append to the list
            toggled_chars.append(char.upper())
    # Join the list into a string and return it
    return ''.join(toggled_chars)

# Given a list of strings, write a function to toggle the case of all characters in each string and then concatenate the results into a single string, with each toggled string separated by a space.
def toggle_and_concatenate(strings):
    # Initialize an empty list to store the toggled strings
    toggled_strings = []
    # Iterate over each string in the list
    for string in strings:
        # Toggle the case of the string and append to the list
        toggled_strings.append(toggle_string(string))
    # Join the list into a single string with each toggled string separated by a space
    return ' '.join(toggled_strings)

assert toggle_and_concatenate(['Hello', 'World']) == 'hELLO wORLD'
assert toggle_and_concatenate(['Python', 'Programming']) == 'pYTHON pROGRAMMING'
assert toggle_and_concatenate(['aBcDeF']) == 'AbCdEf'
assert toggle_and_concatenate(['123', '456']) == '123 456'
assert toggle_and_concatenate([]) == ''