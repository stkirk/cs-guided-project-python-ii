"""
Challenge #9:

Given a string, write a function that returns the "middle" character of the
word.

If the word has an odd length, return the single middle character. If the word
has an even length, return the middle two characters.

Examples:
- get_middle("test") -> "es"
- get_middle("testing") -> "t"
- get_middle("middle") -> "dd"
- get_middle("A") -> "A"
"""
import math

def get_middle(input_str):
    start = math.floor(len(input_str) / 2.01)
    end = math.ceil(len(input_str) / 1.99)
    return input_str[start:end]

def get_middle_convoluted(input_str):
    # Calculate start index
    start = int((len(input_str) - 1) / 2)

    # Calculate end index
    end = int(len(input_str) / 2 + 1)

    # return from start to end
    return input_str[start:end]

print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))
print(get_middle("A"))
