#users
#different types but must be signed in first
#inheritance example, pass the parent class

class User(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('You are logged in')
#character classes
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'attacking with {self.arrows} arrows')

    def run(self):
        print('ran fast')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)



hb1 = HybridBorg('Queen' ,50, 'flame' )

print(hb1.check_arrows())



Wizard1 = Wizard('Merlin', 50,)
Archer1 = Archer('Robin', 100)

#def player_attack(char):
   # char.attack()

#for char in [Wizard1, Archer1]:
 #   char.attack()


