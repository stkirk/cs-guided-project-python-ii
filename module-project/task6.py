# given a start(int) and end(int)
# return the count of all the integers in that range that aren't 5

# letter in "aeiouAEIOU" evaluates to true/false

def intCount(start, end):
    count = 0
    for i in range(start, end + 1):
        if "5" in str(i):
            continue
        else:
            count += 1

    return count
    

print(intCount(1, 5)) #4
print(intCount(1 , 9)) #8
print(intCount(4, 17)) #12
