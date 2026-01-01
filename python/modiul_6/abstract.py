from abc import ABC , abstractmethod
class Animal(ABC):
    @abstractmethod
    def eat(self):
       print('I eat food')
       
    @abstractmethod
    def move(self):
        print('He can move')
    

class Monkey(Animal):
    def __init__(self, name):
        self.category = 'Monkey'
        self.name = name
        super().__init__()
    def eat(self):
        return super().eat()
    def move(self):
        return super().move()

layka = Monkey('Luckey')
layka.eat()