# Python has a print function 
print("I'm Python. Nice to meet you!")

# By default the print function also prints out a newline at the end.
# use the optional argument `end` to change the end string 

print("I'm Python. Nice to meet you.", end="!")

# Getting input from console 
input_string_var = input("Enter some data: ")

# convention in naming variables are snake_case style 
some_var = 5
some_var

# if condiitonal clause can be used as an expression
"yay!" if 0 > 1 else "nay!"


# Lists store sequences 
li = []

# It can be started with a prefilled list 
other_li = [4,5,6,7]

# adding to the end of a list 
other_li.append(1)
other_li
# remover from the end of a list 
other_li.pop() 
other_li

# accessing a list item 
other_li[3]

# look at the last item of a list 
other_li[-1]

# print a range of list items using slices 
# list[start:end:step]

# copy a list to another list variable 
li = other_li[:]

# remove arbitrary items from a list with `del`
del li[3]

# remove the first item of a list 
li.remove(2) # raises a ValueError if the value(2) is not in the list

# insert an element at a specific index 
# list(index, value)
li.insert(1,2) 

# Get the index of the first item found matching the argument 
# li.index(value)
li.index(2)

# you can add lists 
li + other_li

# concatenate lists with `extend()`
li.extend(other_li)

# check for the existence in a list with `in`
1 in li 

# examine the length with "len()"
len(li)

# Tuples are like lists but are immutable 
tup = (1,2,3)

tup[0]

# tuples have a comma after the last element 
type((1,))

len(tup)
tup + (5,6,7,8)
tup[3]
tup[:4]
2 in tup

# Unpacking tuples or lists into variables 
a, b, c = (1, 2, 3)

# You can also do extended unpacking 
a, *b, c = (1, 2, 3, 4) 
# a is 1, b is [2,3], c is 4 

# Now look how easy it is to swap 2 values 
d,e,f = 4,5,6 
e, d = d, e # d is now 5 and e is now 4


# Dictionaries store mappings from keys to values 
empty_dict = {}
filled_dict = {"one": 1, "two": 2, "three": 3}
# keys are immutable and includes ints, floats, strings, tuples 
valid_dict = {(1,2,3): [1,2,3]}
# invalid_dict = {[1,2,3]: "123"} this is not allowed

# look up dictionary values with []
filled_dict["one"]

# Get all dict keys as an iterable with `keys()` by calling and turning it into a list 
list(filled_dict.values()) 

# Check for a key in a dictionary with `in`
"one" in  filled_dict
1 in filled_dict 

# Use `get()` keyword to catch KeyError 
filled_dict.get("four")
filled_dict.get("one")

# The `get()` keyword supports a default value if false 
# dict_name.get(key, default)
filled_dict.get("five", 5)

# The keyword `setdefault()` inserts into a dictioinary only if the given key isn't present 
filled_dict.setdefault("six", 6)
filled_dict.setdefault("five", 5)

# Adding to a dictionary using the `update()`function 
filled_dict.update({"four":4})

# Use `del` to remove keys from a dictionary 
del filled_dict["one"]

# dictionary unpacking 
{"a": 1, **{"b": 2}}
{"a": 1, **{"a": 2}}

# Sets store ...... well sets 
empty_set = set()

# initializing a set with values 
some_set = {1,1,2,2,3,4}

# set values are immutable, hence you cant put a list in a set 
# invalid_set = {[1], 1}
valid_set = {(1,), 1}

# Use the `add()` to add items to a set 
filled_set = some_set
filled_set.add(5)

# sets do not allow duplicates 
filled_set.add(5)

# Use `&` for set intersections 
other_set = {3, 4, 6}
filled_dict & other_set

# Use `|` for set unions 
filled_set | other_set

# Use `-` for set differnce 
filled_set - other_set 

# Use `^` for set symmetric difference with 
filled_set ^ other_set 

# Check if left set is a superset of the right set 
{1,2,} >= {1,2,3}

# Check if set on the left is a subset of the right set 
{1,2} <= {1,2,3}

# Check for a iten in a set with `in`
2 in filled_set

# Make a one layer set deep copy
filled_set = some_set.copy()
filled_set is some_set

