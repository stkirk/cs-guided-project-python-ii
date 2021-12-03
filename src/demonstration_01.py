"""
Challenge #1:

Write a function that retrieves the last n elements from a list.

Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid"
- last([1, 2, 3, 4, 5], 0) ➞ []

Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.
"""


def last(a, n):
    # Return "invalid" if n exceeds the length of the list.
    if n > len(a):
        return "invalid"
    # Return an empty list if n == 0.
    elif n == 0:
        return []
    else:
        '''
        # long way
        # figure out the start index i
        # i is n indexes back from the last index of the list-->len(a)
        i = len(a) - n

        # sublist i to j
        # return from start index i --> last index of the list--> len(a)
        return a[i:len(a)]
        '''
        # pseudo --> return a[n indexes from the end:to the end]
        return a[-n:]

        # Think of the slicing operator as a function --> slice(start, end, stepSize) where only the first arg is required
        # Excluding arguments is like calling the function without arguments, using default end value-->len(iterable) and default-->stepSize(1)

print(last([1, 2, 3, 4, 5], 1))
print(last([4, 3, 9, 9, 7, 6], 3))
print(last([1, 2, 3, 4, 5], 7))
print(last([1, 2, 3, 4, 5], 0))