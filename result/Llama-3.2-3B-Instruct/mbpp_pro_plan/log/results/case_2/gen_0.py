# Write a function to toggle the case of all characters in a string.
def toggle_string(string):
    # Initialize an empty string to store the result
    result = ""
    
    # Iterate over each character in the input string
    for char in string:
        # Check if the character is an uppercase letter
        if char.isupper():
            # If it is, convert it to lowercase
            result += char.lower()
        # Check if the character is a lowercase letter
        elif char.islower():
            # If it is, convert it to uppercase
            result += char.upper()
        # If the character is not a letter, leave it as is
        else:
            result += char
    
    # Return the resulting string
    return result

# Given a list of strings, write a function to toggle the case of all characters in each string and then concatenate the results into a single string, with each toggled string separated by a space.
def toggle_and_concatenate(strings):
    # Initialize an empty list to store the toggled strings
    toggled_strings = []
    
    # Iterate over each string in the input list
    for string in strings:
        # Call the toggle_string function to toggle the case of the current string
        toggled_string = toggle_string(string)
        # Append the toggled string to the list
        toggled_strings.append(toggled_string)
    
    # Join the toggled strings into a single string, separated by spaces
    result = " ".join(toggled_strings)
    
    # Return the resulting string
    return result

assert toggle_and_concatenate(['Hello', 'World']) == 'hELLO wORLD'
assert toggle_and_concatenate(['Python', 'Programming']) == 'pYTHON pROGRAMMING'
assert toggle_and_concatenate(['aBcDeF']) == 'AbCdEf'
assert toggle_and_concatenate(['123', '456']) == '123 456'
assert toggle_and_concatenate([]) == ''