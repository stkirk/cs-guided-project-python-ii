print("-----------Task 2----------------")
# given a number of years(int) and numbers of groups(int) in a year
# For each year number, follow with a group
# denote groups with a letter (group 1 is a, group 2 is b, etc.), if groups input number is 4 there are a, b, c, and d groups in each year
# return a comma seperated string of yearGroups ("1a, ) for every year
# maximum number of years is 10 and groups is 26

# chr(97) == 'a'
# chr(122) == 'z'
# chr(97 + index) == alpha according to index

def groupGenerator(years, groups):
    # conditionals:
    if years < 1 or years > 10:
        return "1 <= years <= 10"
    elif groups < 1 or groups > 26:
        return "1 <= groups <=26"
    else:
        # turn years integer into a list of lists of years
        listOfLists = []
        for i in range(1, years + 1):
            listOfLists.append([str(i) + chr(97 +group) for group in range(groups)])
        # iterate through the list of lists, adding each list to the last to make one big list
        masterList = []
        for i in listOfLists:
            masterList += i
        
        # join together masterList indices to make a string
        stringList = ', '.join(masterList)

        return stringList

print(groupGenerator(7, 4))
print(groupGenerator(2, 26))
print(groupGenerator(220, 2))
print(groupGenerator(3, 27))
