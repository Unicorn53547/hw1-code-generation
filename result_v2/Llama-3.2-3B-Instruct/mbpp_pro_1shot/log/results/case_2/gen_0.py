# Write a function to toggle the case of all characters in a string.
def toggle_string(string):
    return ''.join([char.swapcase() for char in string])

assert toggle_and_concatenate(['Hello', 'World']) == 'hELLO wORLD'
assert toggle_and_concatenate(['Python', 'Programming']) == 'pYTHON pROGRAMMING'
assert toggle_and_concatenate(['aBcDeF']) == 'AbCdEf'
assert toggle_and_concatenate(['123', '456']) == '123 456'
assert toggle_and_concatenate([]) == ''