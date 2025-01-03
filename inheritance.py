            # Inheritance 

"""Inheritance allow defined classes to inherit 
methods and variables from their parent class.
To take advantage of modularization by file, we put classes
in their own files and import them where we want to use them."""

from human import Human

# specify the parent class(es) as params to the class definition 
class Superhero(Human):
    # To inherit all of the parents definitions without any changes use `pass`
    species = "Superhuman"

    # adding more args or params 
    def __init__(self, name, movie=False, 
                superpowers=["super strength", "bulletproofing"]):
        # additional class attr
        self.fictionall = True 
        self.movie = movie 
        # beware of default shared values/variables
        self.superpowers = superpowers

        # use `super` keyword to access parent class methods
        super().__init__(name)

    # overidding the sing method/function 
    def sing(self):
        return "Dun, dun, DUN!"
    
    def say(self):
        return "Tick: "
    
    # add an additional instance method 
    def boast(self):
        for power in self.superpowers:
            print("I wield the power of {pow}!".format(pow=power))


if __name__ == "__main__":
    sup = Superhero(name="Tick")

    # instance type checks
    if isinstance(sup, Human):
        print("I am human")
    if type(sup) is Superhero:
        print("I am a superhero")

    # Use `getattr()` and super() for method resolution order to determine how classes are searched for attr and methods 
    print(Superhero.__mro__)

    # Call parent method with own class 
    print(sup.species)

    # call overridden method 
    print(sup.sing())

    # call method from Human class 
    sup.say()

    # call method that exists only in Superhero
    sup.boast()

    # Inherited class attr
    sup.age = 31
    print(sup.age)

    # attr that only exist in Superhero
    print("Am I Oscar eligible? "+ str(sup.movie))



# Multiple Inheritance 

class Bat:
    species = "Baty"
    def __init__(self, can_fly=True):
        self.fly = can_fly

    # This class also has a say method 
    def say(self, msg):
        msg = "... ... ..."
        return msg
    
    # And its own method as well
    def sonar(self):
        return "))) ... ((("
    
b = Bat()
print(b.say("hello"))
print(b.fly)

# Another class thaat inherits from superhero and bat 
from . import Superhero
from . import Bat 

# defining batman as a child that inherits from both superhero and bat 
class Batman(Superhero, Bat):
    def __init__(self, *args, **kwargs):
        # use `super` to inherit from a single parent and use 
        # __init__ to inherit from multiple parents / calling all ancestors
        Superhero.__init__(self, "anonymous", movie=True,
                        superpowers=["Wealthy"], *args, **kwargs)
        Bat.__init__(self, *args, can_fly=False, **kwargs)
        # Overide the value for the name attribute
        self.name = "Sad Affleck"
    
    def sing(self):
        return "nan nan nan nan nan batman!"
    

# method resolution order (MRO) 
print(Batman.__mro__)

# call  parent method whiles using its own class attributes
print(sup.get_species())

# call overridden method 
print(sup.sing())

# call method from human 
sup.say("I agree")
