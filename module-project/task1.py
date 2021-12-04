print("-----------Task 1----------------")
# given a list of names(str), search for the name "Bob" and return its index in the list
# if "Bob" isn't in the list return -1

def bobSearch(names):
  # iterate through the list, if index == "Bob" return the index, else continue
  bob = -1
  for (i, name) in enumerate(names):
    if name == "Bob":
      bob = i
    else:
      continue
  return bob

print(bobSearch(["Jimmy", "Layla", "Bob"])) #2
print(bobSearch(["Bob", "Layla", "Kaitlyn", "Patricia"])) #0
print(bobSearch(["Jimmy", "Layla", "James"])) # -1