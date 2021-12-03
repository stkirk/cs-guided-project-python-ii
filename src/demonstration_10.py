"""
Challenge #10:

Given a string of space separated integers, write a function that returns the
maximum and minimum integers.

Example:
- max_and_min("1 2 3 4 5") -> "5 1"
- max_and_min("1 2 -3 4 5") -> "5 -3"
- max_and_min("1 9 3 4 -5") -> "9 -5"

Notes:
- All inputs are valid integers.
- There will always be at least one number in the input string.
- The return string must be two numbers separated by a single space, and
the maximum number is first.
"""
def max_and_min(input_str):
    # split the string into a list on ints
    numList = input_str.split() #default behavior of split is by an empty space
    # ("1 2 3 4 5") --> ['1', '2', '3', '4', '5']

    # typecast the list of strings into integers
    intNumList = [ int(num) for num in numList]

    # built in methods to iterate through a list and find the min and max values
    listMin = min(intNumList) # returns an integer
    listMax = max(intNumList) # returns an integer

    # return the min and max in an f string
    return f'{listMax} {listMin}'


print(max_and_min("1 2 3 4 5"))
print(max_and_min("1 2 -3 4 5"))
print(max_and_min("1 9 3 4 -5"))
