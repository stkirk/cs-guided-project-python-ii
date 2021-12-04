# given a string of words return the length(int) of the shortest word (s)

def shortFinder(input_str):
    # split into list of individual words
    wordList = input_str.split()
    # loop through each word in list
    shortest = 1
    for (i, word) in enumerate(wordList):
        if i == 0:
            shortest = len(word)
        elif len(word) <= shortest:
            shortest = len(word)
        else:
            continue
    return shortest

print(shortFinder("welcome to a jungle")) #1
print(shortFinder("it is fine")) #2
print(shortFinder("The small red fox jumped over the lazy")) #3