class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age 
        self.height = height
        self.weight = weight
    def eat(self):
        print('Eat beriany fruits polaw')


    def exercise(self):
        raise NotImplementedError


class Cricketer(Person):
    def __init__(self, name, age, height, weight, team):
        self.team = team
        super().__init__(name, age, height, weight)

    def eat(self):
        print('vegitables') #override

    def exercise(self):
        print('GYM ee jaiya poisa furai')

    def __add__(self, other):
        return self.age + other.age
    
    def __mul__(self, other):
        return self.weight * other.weight
    def __len__(self):
        return self.height
    
    def __gt__(self, other):
        return self.age > other.age


shakib = Cricketer('sakib', 22, 86,91,'BD' )
mushi = Cricketer('Musfique',24, 56, 91, 'BD')
shakib.eat()
shakib.exercise()
mushi.eat()
mushi.exercise()


print(55 + 45)
print('jONEY' + 'rONEY')
print([12 , 88] + [3 ,5,61,12])
print(len(shakib))
print(shakib > mushi)