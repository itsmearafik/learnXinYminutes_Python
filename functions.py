# functions are initialised with the `def` keyword 

def add(x,y):
    print("x is {} and y is {}".format(x,y))
    return x + y 

# calling the add function with parameters 
add(2,3)

print("______end of line______")

# another way to call a function is with the keyword arguments 
add(y=6, x=5)

print("______end of line______")

# defining a function that takes a variable number of positional arguments 
def varargs(*args):
    return args 

varargs(1,2,3)
print(varargs(4,5,6,7,8))

print("______end of line______")

# definining a function that takes a variable number of keyword arguments 
def keyword_args(**kwargs):
    return kwargs

# calling the keyword_args function 
keyword_args(big="foot", loch="ness")
print(keyword_args(fname="arafik", lname="alhassan"))

print("______end of line______")

# defining all args in a function
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)

all_the_args(1,2, a=3, b=4)

print("______end of line______")

# Use * to expand args (tuples) and Use ** to expand *args, **kwargs (dictionaries)
args = (1,2,3,4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args)
all_the_args(**kwargs)
all_the_args(*args, **kwargs)

print("______end of line______")

# Returning multiple values (with tuple assignments )

def swap(x, y):
    return y, x 

x = 1
y = 2
x, y = swap(x,y)
print(swap(x,y))

print("______end of line______")

# Global scope 
x = 5  
def set_x(num):
    # local scope begins here 
    x = num 
    print(x)

def set_global_x(num):
    # global keyword indicates that a particular var lives in the global scope
    global x 
    print(x)
    x = num 
    print(x)

set_x(43)

print("______end of line______")

set_global_x(6)

print("______end of line______")

# Python has first class functions 
def create_adder(x):
    def adder(y):
        return x + y 
    return adder 

add_10 = create_adder(10)
print(add_10(3))

print("______end of line______")

# closures in nested functions can use nonlocal keyword to work with variables in nested scope
# which should not be declared in the inner functions 

def create_avg():
    total = 0
    count = 0
    def avg(n):
        nonlocal total, count 
        total += n 
        count += 1 
        return total/count
    return avg

avg = create_avg()
print(avg(3))

print("______end of line______")
print(avg(5))
print(avg(7))

print("______end of line______")

# Built in higher order functions
list(map(add_10, [1,2,3]))
list(map(max, [1,2,3], [4,2,1]))
list(filter(lambda x: x > 5, [3, 4, 5, 6,7]))

print("______end of line______")
print(list(map(add_10, [1,2,3])))
print(list(map(max, [1,2,3], [4,2,1])))
print(list(filter(lambda x: x > 5, [3, 4, 5, 6,7])))

print("______end of line______")

# list comprehensions stores the output as a list(which itself may be nested )
# List comprehensions can also be used for maps and filters 
[add_10(i) for i in [1,2,3]]
[x for x in [3, 4, 5, 6, 7] if x > 5]

print([add_10(i) for i in [1,2,3]])
print([x for x in [3, 4, 5, 6, 7] if x > 5])

print("______end of line______")

# using list comprehensions to construct set and dict comprehensions 
{x for x in "abcddeer" if x not in "abc"}
{x: x**2 for x in range(5)}

print({x for x in "abcddeef" if x not in "abc"})

print("______end of line______")

print({x: x**2 for x in range(5)})
print("______end of line______")