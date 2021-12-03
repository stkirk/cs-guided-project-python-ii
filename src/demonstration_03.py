"""
Challenge #3:

Given a string of numbers separated by a comma and space, return the product of the numbers.

Examples:
- multiply_nums("2, 3") ➞ 6
- multiply_nums("1, 2, 3, 4") ➞ 24
- multiply_nums("54, 75, 453, 0") ➞ 0
- multiply_nums("10, -2") ➞ -20

Notes:
- Bonus: Try to complete this challenge in one line!
"""


def multiply_nums_long(nums):
    # Initialize the product
    product = 1

    # Seperate the string into a list of numbers, using 'comma, space' (', ') as a seperator
    numberList = nums.split(', ')

    # cast each index (which is still a string at this point) to an integer and multiply those numbers together
    for i in numberList:
        product *= int(i)

    return product

# alternate solution
def multiply_nums(nums):
    # ("1, 2, 3, 4") --> ("1*2*3*4")
    codeString = nums.replace(', ', "*") # turns "2, 3" into "2*3"
    # eval takes a string argument and runs it like python code for everything inside the quotes
    return eval(codeString)

print(multiply_nums("2, 3"))
print(multiply_nums("1, 2, 3, 4"))
print(multiply_nums("54, 75, 453, 0"))
print(multiply_nums("10, -2"))
