class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.mydict = {
            'name': 'Yoyo',
            'has_pets': False
        }


    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __call__(self):
        return 'yes?'

    def __getitem__(self, i):
        return self.mydict[i]


action_figure = Toy('red', 0)


print(action_figure['name'])




