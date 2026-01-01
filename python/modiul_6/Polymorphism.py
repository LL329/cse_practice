class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print('Animal making some sound')

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print('meow meow')

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print('Ghew gheu')

class Goat(Animal):
    def __init__(self, name):
        super().__init__(name)


    def make_sound(self):
        print('Beh Beh Beh')
        
        

dogy = Cat('REal don')
dogy.make_sound()


shephard = Dog('Local don')
shephard.make_sound()

messi = Goat('L M')
messi.make_sound()

less = Goat('Gora gori khai')


Animals = [dogy, shephard, messi, less]
for animal in Animals:
    animal.make_sound()
    