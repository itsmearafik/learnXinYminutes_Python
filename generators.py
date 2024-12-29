""" Generators are memory efficient because they only load the data needed to
    process the next value in the iterable. This allows them to perform operations on 
    otherwise prohibitively large value ranges.
"""
def double_numbers(iterable):
    for i in iterable:
        yield i + i 

for i in double_numbers(range(1, 900000000)):
    print(i)
    if i >= 30:
        break 

# create generator comprehensions 
values = (-x for c in [1,2,3,4,5])
gen_to_list =  list(values)
print(gen_to_list)

# wrappers are one type of decorators 
# that adds logging to existing functions without modifying them  

def log_function(func):
    def wrapper(*args, **kwargs):
        print("Entering function", func.__name__)
        result = func(*args, **kwargs)
        print("Exiting function", func.__name__)
        return result
    return wrapper 

@log_function
def my_function(x,y):
    return x + y 

# To fix the issue of getting information about a function, we us functools

from functools import wraps 

def log_function(func):
    return x + y 

my_function(1,2)
print(my_function.__name__)
print(my_function.__code__)