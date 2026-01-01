class User:
    def __init__(self, name, age, money):
        self.name = name
        self._age = age
        self.money = money

    @property
    def age(self):
        return self._age
    
    @property
    def salary(self):
        return self.money
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            return 'salary can\'t be negative'
        self.money += value
    
samsu = User('Kopaiya vaj kore fal', 77, 12000)
print(samsu.age)
print(samsu.salary)
samsu.salary = 1000
print(samsu.salary)