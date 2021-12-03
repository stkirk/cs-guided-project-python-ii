"""
Challenge #6:

Return the number (count) of vowels in the given string.

We will consider `a, e, i, o, u as vowels for this challenge (but not y).

The input string will only consist of lower case letters and/or spaces.
"""
def get_count(input_str):
    # letter in "aeiouAEIOU" evaluates to True if that index is one of those letters
    # True when being summed typecasts to a 1, so for each index that is in that subset 1 is added to the sum
    return sum(letter in "aeiouAEIOU" for letter in input_str)

def verbose_get_count(input_str):
    # 
    vowelCount = 0
    for letter in input_str:
        # if the index is one of these letters...increment the vowelCount
        if letter in "aeiouAEIOU":
            vowelCount += 1
    return vowelCount
        

print(get_count("aeiou")) #5
print(get_count("trgbw$")) #0
print(get_count("a and b")) #2
print(get_count("jsaldjlksaj#@$@#$___ sajdflsa &#(Fjklfjls")) #??? 
