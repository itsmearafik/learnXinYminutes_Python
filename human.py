class Human:
    # A class attribute is shared by all instances of this class 
    species = "H. sapiens"
    """ Basic initializer is when a class is instantiated
    the double leading and trailing underscores denote objects or attributes 
    that are used by Pyhton but live in a user-controlled namespaces.
    special(dunder) methods are methods(objects or attributes) like __init__, __str__

    """
    def __init__(self, name):
        # assign the arg to the isinstance's name attr 
        self.name = name 

        # initialize property 
        self._age = 0
        # The leading underscore show the `age` property is to be used internally.
        # This is a hint to other devs 

        # an instance method (al methods take self as first arg)
        def say(self, msg):
            print("{name}: {message}".format(name=self.name, message=msg))

        def sing(self):
            return "yo... yo... microphone check.... one two.. one two..."
        
        # A class method is shared among all instances and a re called with the calling class as the first arg
        @classmethod
        def get_species(cls):
            return cls.species 
        
        # A staticmethod is called without a class or instance reference 
        @staticmethod 
        def grunt():
            return "*grunt*"
        
        # a property is just like a getter: it turns the method age() into a read-only attr of the same name.
        @property
        def age(self):
            return self._age 
        
        # This allows the property to be set 
        @age.setter
        def age(self, age):
            self._age = age 

        # This allows the property to be deleted
        @age.deleter
        def age(self):
            del self._age 

        # The    `__name__` check makes sure this code block is only executed when the modeule is the main program
        if __name__ == "__main__":
            # instance of the Human objects 
            i = Human(name="abdul")
            i.say("Abdul says Hi")
            j = Human("Joel")
            j.say("Joel says Hello")
            # i and j are instances of type human; i.e they are human objects 

            # class methods 
            i.say(i.get_species())
            # change the shared attr 
            Human.species = "H. neanderthalensis"
            i.say(i.get_species())
            j.say(j.get_species())

            # call the static method 
            print(Human.grunt())
            print(i.grunt())

            # update the property for this instance 
            i.age = 42 
            # Get the property 
            i.say(i.age)
            j.say(j.age)

            del i.age 

