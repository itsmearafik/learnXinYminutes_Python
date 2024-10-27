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
with open("myfile.txt") as f:
    for line in f:
        print(line)