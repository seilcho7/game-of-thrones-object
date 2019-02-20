# name
# avatar (profile picture)
# inventory

# def do_stuff():
#   pass

class Character():
    # "dunder" init method is the constructor
    def __init__(self, new_name, new_avatar):
        # "self" is the customary way to refer to the instance being built
        # in some other languages, they use "this"
        self.name = new_name
        self.avatar = new_avatar
        self.inventory = []
    
    # 'someone=None' is default argument
    # 'None' is equivalent to 'null' in other languages
    def greet(self, someone=None):
        # When we assume that 'someone' argument has a '.name' property
        # this is an Object-Oriented Programming principle called
        # polymorphism.
        # In python, it's called "Duck Typing"
        if someone is not None:
        # if someone:
            return "Hello, %s, I am %s. I am awesome." % (someone.name, self.name,)
            
        else:
            return "Hello, I am %s. I am awesome." % (self.name,)

# Hero is a kind of Character
# Hero is a subclass of Character
# Hero inherits from Character
# Character is the super class of Hero
class Hero(Character):
    pass

# Monster is kind of Character
# Monster is a subclass of Character
# Monster inherits from Character
class Monster(Character):
    pass