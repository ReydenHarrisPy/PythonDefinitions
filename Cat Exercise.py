#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
Cat1 = Cat('Doja', 5)
Cat2 = Cat('Selena Kyle', 15)
Cat3 = Cat('Olivia Pope', 7)


# 2 Create a function that finds the oldest cat

def OldestCat(*args):
    return max(*args)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f'the oldest cat is {OldestCat(Cat3.age,Cat2.age,Cat1.age)}')
