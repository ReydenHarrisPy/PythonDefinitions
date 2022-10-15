#OOP
#think of a class as a blueprint:
class PlayerCharacter:
    membership = True #this is a class object attribute. Doesn't change across instances.
    def __init__(self, name='anonymous', age=0): #this is a dunder method, constuctor method
        if (age > 18):
            self.name = name #name attribute
            self.age = age # age attribute

    def run(self, name):
        print('run')
        return ''

    def shout(self, name, age):
        print(f'my name is {self.name}')
        return ""


Player1 = PlayerCharacter('Reyden', 19) #instantiate instance of a player, calling class to create an object
Player2 = PlayerCharacter('Bryan', 25)

#print(Player1.age)
#print(Player1.name)
#print(Player2.age)
#print(Player2.name)

print(Player1.age)

print(Player1.run("reyden"))