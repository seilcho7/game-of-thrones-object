from character import Character
from character import Hero

# Characters can be instantiated with name and avatar

arya = Character("Arya Stark", "arya.png")
jon = Character("Jon Snow", "jon.png")

print(arya.name, arya.avatar)
print(jon.name, jon.avatar)

# After adding 2 items to inventory
# length of inventory should == 2

arya.inventory.append('sword')
arya.inventory.append('mask')

print(len(arya.inventory))

# arya should have a 'greet' method 
# and when I call with 'arya.greet(jon)', it should return
# "Hello, Jon Snow, I am Arya Stark. I am awesome."
print(arya.greet(jon))

# arya should have a 'greet' method 
# and when I call with 'arya.greet()', it should return
# "Hello, I am Arya Stark. I am awesome."
print(arya.greet())

# I should be able to create a Hero instance
bronn = Hero("Bronn of the Blackwater", "bron.png")

# Hero should be able to greet Character
print(bronn.greet(arya))
print(jon.greet(bronn))