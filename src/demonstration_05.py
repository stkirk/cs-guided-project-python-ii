"""
Challenge #5:

Create a function that returns the data type of a given argument. There are
seven data types this challenge will be testing for:

- List
- Dictionary
- String
- Integer
- Float
- Boolean
- Date

Examples:
- data_type([1, 2, 3, 4]) ➞ "list"
- data_type({'key': "value"}) ➞ "dictionary"
- data_type("This is an example string.") ➞ "string"
- data_type(datetime.date(2018,1,1)) ➞ "date" 

Notes:
- Return the name of the data type as a lowercase string.
"""

# datetime is a module that you need to import
import datetime

def data_type(value):
    # isinstance takes two arguments, the thing you are evaluating and the data type you are comparing it to
    # if the thing you are evaluating is the same type as the second argument it will evaluate to True
    if isinstance(value, list):
        return "list"
    elif isinstance(value, dict):
        return "dictionary"
    elif isinstance(value, str):
        return "string"
    elif isinstance(value, int):
        return "integer"
    elif isinstance(value, float):
        return "float"
    elif isinstance(value, bool):
        return "boolean"
    elif isinstance(value, datetime.date):
        return "datetime"
    else:
        return "unknown"


print(data_type([1, 2, 3, 4]))
print(data_type({'key': "value"}))
print(data_type("This is an example string."))
print(data_type(datetime.date(2018,1,1)))
