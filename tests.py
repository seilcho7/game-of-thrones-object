from character import Character
from character import Hero
from character import Monster
from character import MinorHero

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

# I should be able to create a Monster instance
pinky = Monster()

# Monster should be able to greet Hero
print(pinky.greet(bronn))
print(bronn.greet(pinky))

# Expect Bronn to say "EEEEEEEK!"
# when encountering a monster
print(bronn.greet(pinky))
print(bronn.greet(jon))

print("###########")

ralph = MinorHero()
print(ralph.greet(bronn))