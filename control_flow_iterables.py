"""Control Flow and Iterables"""

some_var = 5

# for conditionals, functions, etc the convention is to use four spaces not tabs 

if some_var > 10:
    print("some_var is totally bigger than 10.")
elif some_var < 10:
    print("some_var is smaller than 10.")
else:
    print("some_var is indeed 10.")


""" For loops iterate over lists """
mammals = ["dog", "cat", "mouse"]

for animal in mammals:
    print("{} is a mammal".format(animal))


for cart in ["washing soap", "detergent","sponge", "hand gloves"]:
    print("{} is part of your shop items".format(cart).capitalize())