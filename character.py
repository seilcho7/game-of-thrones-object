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
        if someone is not None:
        # if someone:
            return "Hello, %s, I am %s. I am awesome." % (someone.name, self.name,)
            
        else:
            return "Hello, I am %s. I am awesome." % (self.name,)