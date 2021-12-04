# given an array of integers:
# return the sum of all the positive integers
# if no positive integers in the list, the sum is 0

def sumPositives(input_arr):
    sum = 0
    for i in input_arr:
        if i < 0:
            continue
        else:
            sum += i
    return sum

print(sumPositives([1, 2, 3, -4, 5])) #11
print(sumPositives([-3, -2, -1, 0, 1])) # 1
print(sumPositives([-3, -2])) # 0