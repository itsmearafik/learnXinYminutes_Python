""" 
This is the Begiining of the Learn X in Y minutes for python repo
"""

# 1. Primitive Datatypes and Operations 

# Numbers 
1 + 1 
10 - 2 

39 / 3  # the result for division is always float 

# floor division 
5 // 3  # 1
-5 // 3  # -2
5.0 // 3.0 # 1.0 

# Modulo operation 
7 % 3 # 1

# i % j have the same sign as j
-7 % 3 # 2

# Exponentiation (x**y, x to the yth power)
2**3  # 8

# Enforce precedence with parentheses
1 + 3 * 2  # 7

(1 + 3) * 2  # 8

# Boolean values are primitives (Note: the capitalizations)
True 
False 

# negate with not 
not True  # False 
not False # True 

# Note "and" & "or" are case-sensitive 
True and False  # False
False or True   # True 
#True and False are actually 1 and 0 but with different keywords

# Comparison operators look at the numerical value of True and False 
0 == False # True
2 > True # True
-5 != False # True

'''
None, 0, and empty strings,lists,dicts,tuples,sets all evaluate to False
'''
# All other values are True 
bool(0)  # False
bool("")  # False
bool([])  # False
bool(())   # False 
bool({})   #False 
bool(set())  # False 
bool(4)  # True 
bool(-6)  # True 

# Using boolean logical operators operators on ints casts them to booleans foe evaluation
# but their non-cast value is returned. bool(ints) is different from bitwise 

bool(0)  # False
bool(2)  # True
0 and 2 # 0
-5 or 0 # -5


# Equality is ==
1 == 1 # True 
2 == 1 # False 

# Inequality is != 
1 != 1 # True
2 != 1 # True

# More comparisons 
1 < 10 # True
1 > 10  # False 
2 <= 2 # True 
2 >= 2 # True 

# Selecting whether a value is in a range 
1 < 2 and 2 < 3 # True 
2 < 3 and 3 < 2 # False 

# Chaining makes this statement look nicer 
1 < 2 < 3 # True 
2 < 3 < 2  # False

""" 
is : checks if 2 variables refer to the same object 
== : checks if the object pointed to have the same values.
"""

a = [1, 2, 3, 4]  # Point a at a new list [1,2,3,4]
b = a  # Point b at what a is pointing to
b is a # True, a and b refer to the same object
b == a # True, a's and b;s objects are equal
b = [1,2,3,4] # Point b at a new list [1,2,3,4]
b is a # False, a nd b do not refer to the same object
b == a # True, a's and b's objects are equal

# Strings are created with " or '
"This is a string"
'This is also a string'

# Strings can be added too 
"Hello " + "world"  # "Hello world"
# String literals (but not variables) can be concatenated without using '+'

"Hello " "world"  # "Hello world"

# A string can be treated like a list of characters 
"Hello world!"[0]  # 'H'


# You can find the length of a string 
len("This is a string")

# Using of formatted string literals (f-strings)
name = "arafik"
f"My name is {name}"

# None is an object 
None # None

# Don't use the equality "==" symbol to compare objects to None
# USe "is" instead. This checks for equality if object identity. 
"etc" is None # False
None is None # True 
