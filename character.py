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
    
    def greet(self, someone):
        return "Hello, %s, I am %s. I am awesome." % (someone.name, self.name,)