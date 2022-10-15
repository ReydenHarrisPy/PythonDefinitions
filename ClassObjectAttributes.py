#OOP
#think of a class as a blueprint:
class PlayerCharacter:
    membership = True #this is a class object attribute. Doesn't change across instances.
    def __init__(self, name, age): #this is a dunder method, constuctor method
        if self.membership:
            self.name = name #name attribute
            self.age = age # age attribute
    def run(self):
        print('run')
        return ''

    def shout(self):
        print(f'my name is {self.name}')
        return ""


Player1 = PlayerCharacter('Reyden', 28) #instantiate instance of a player, calling class to create an object
Player2 = PlayerCharacter('Bryan', 32)
#print(Player1.age)
#print(Player1.name)
#print(Player2.age)
#print(Player2.name)

print(Player2.shout())
print(Player1.run())