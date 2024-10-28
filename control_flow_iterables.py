"""Control Flow and Iterables"""

some_var = 5

# for conditionals, functions, etc the convention is to use four spaces not tabs 

if some_var > 10:
    print("some_var is totally bigger than 10.")
elif some_var < 10:
    print("some_var is smaller than 10.")
else:
    print("some_var is indeed 10.")


print("______end of line______")

""" For loops iterate over lists """
mammals = ["dog", "cat", "mouse"]

for animal in mammals:
    print("{} is a mammal".format(animal))

print("______end of line______")

for cart in ["washing soap", "detergent","sponge", "hand gloves"]:
    print("{} is part of your shop items".format(cart).capitalize())


print("______end of line______")
# `range(number)` returns an iterable of numbers from zero up to (excluding) the given number

for i in range(4):
    print(i)

print("______end of line______")
# `range(lower, upper)` returns an iterable from the lower number to the upper number 

for i in range(4,8):
    print(i)

print("______end of line______")
# `range(lower, upper, step)` returns an iterable of numbers from the lower number to the upper number, while incrementing by step.The default step value is 1 if its not indicated

for i in range(4,8,2):
    print(i)

print("______end of line______")


# Loop over a list to retrieve both the index and the value of each list item

animals = ["dog", "cat", "mouse"]
for i, value in enumerate(animals):
    print(i, value)

print("______end of line______")

cart = ["washing soap", "detergent","sponge", "hand gloves"]
for i, value in enumerate(cart):
    print("{} {} is part of your shop items".format(i+1,value.capitalize()))

print("______end of line______")

# While loops go until a condition is no longer met 

x = 0
while x < 4:
    print(x)
    x += 1 # this is a shorthand for x = x + 1 

print("______end of line______")

# Handle exceptions with a try/except block 
try:
    while x < 8:
        print("X is currently: ",x)
        x += 1
    # use `raise` to raise an error 
    raise IndexError("This is an index error")
except IndexError as e:
    pass # Refrain from not providing a recovery exception options
except (TypeError, IndexError):
    pass # multiple exceptions can be processed jointly
else:
    pass # optional clause to the try/except block. Must follow all except blocks.
    print("All good") #Runs only if the code in try raises no exceptions
finally: # it executes under all circumstances 
    print("We can clean up resources here")


# You can use `with` stetement intead of try/finally to cleanup resources 
with open("./myfile.txt") as f:
    for line in f:
        print(line)

# Writing to a file, Working with files 
contents = {"aa": 12, "bb": 21}
with open("./myfile1.txt", "w") as file:
    file.write(str(contents)) # writes a string to a files
    file.write("My name is arafik")

import json 
with open("myfile2.txt", "w") as file:
    file.write(json.dumps(contents))

print("______end of line______")
    
# Reading from a file 
with open("./myfile1.txt") as file:
    contents = file.read()

print(contents)

print("______end of line______")

with open("./myfile2.txt", "r") as file:
    contents = json.load(file)
print(contents)


print("______end of line______")

# An iterable is an object that can be treated as a sequence

filled_dict = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict.keys()
print(our_iterable) # This returns an object that implements an iterable interface

print("______end of line______")

# looping over iterables 
for i in our_iterable:
    print(i) # Prints one, two, three [ iterabls ]


print("______end of line______")

# Iterables cannot be accessed by the index method 
try:
    our_iterable[1]
except:
    print("Iterables elements cannot be addressed by the index")


print("______end of line______")

# An iterable is an object that can create an iterator 
our_iterator = iter(our_iterable)

print("______end of line______")

# Iterators is an object that can remember the state as we traverse through
# You can get the next object of an iterator with the `next()` keyword 

next(our_iterator)

print("______end of line______")
next(our_iterator)

print("______end of line______")
next(our_iterator)
# The iterator raises a StopIteration exception after it has returned all of its data. 

print("______end of line______")
# Using the for loop to loop over an iterable 
# The `for` keyword loops over the iterable implicitly 
our_iterator = iter(our_iterable)

for i in our_iterator:
    print(i)


print("______end of line______")
# You can grab all the elements of an iterable or iterator by call of a list()
list(our_iterable)
print(list(our_iterable))
print("______end of line______")
list(our_iterator)
print(list(our_iterator))

print("______end of line______")