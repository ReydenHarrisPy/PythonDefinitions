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


    @classmethod
    def adding_things(cls, num1, num2):
        return cls('teddy',num1 + num2)

    @staticmethod
    def adding_things(num1, num2):
        return num1 + num2


Player1 = PlayerCharacter('Reyden', 19) #instantiate instance of a player, calling class to create an object
Player2 = PlayerCharacter('Bryan', 25)

Player3 = PlayerCharacter.adding_things(2,3)

print(Player3.name)


