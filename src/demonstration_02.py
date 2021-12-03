"""
Challenge #2:

Given a list of numbers, create a function that returns the list but with each
element's index in the list added to itself. You should add 0 to the number at
index 0, add 1 to the number at index 1, etc.

Examples:
- add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]
- add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]
- add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]

Notes:
- The input list will only contain integers.
"""


def add_indexes(numbers):
    # Start a new list
    # solution = []
    # # Loop through original numbers list adding a v
    # for (i, num) in enumerate(numbers):
    #     solution.append(i + num)
    # return solution

    # List comprehension version, return a new list and in that list:
    # add indexValue(num) + indexNumber(i) for (indexNumber(i), numberValue(num)) in enumerate(numbers) 
    return [num + i for (i, num) in enumerate(numbers)]

print(add_indexes([0, 0, 0, 0, 0]))
print(add_indexes([1, 2, 3, 4, 5]))
print(add_indexes([5, 4, 3, 2, 1]))
