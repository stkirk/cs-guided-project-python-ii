"""
Challenge #6:

Return the number (count) of vowels in the given string.

We will consider `a, e, i, o, u as vowels for this challenge (but not y).

The input string will only consist of lower case letters and/or spaces.
"""
def get_count(input_str):
    # 
    count = 0
    for letter in input_str:
        if letter in "aeiouAEIOU":
            count += 1
    return count
        

print(get_count("aeiou")) #5
print(get_count("trgbw$")) #0
print(get_count("a and b")) #2
print(get_count("jsaldjlksaj#@$@#$___ sajdflsa &#(Fjklfjls")) #??? 
