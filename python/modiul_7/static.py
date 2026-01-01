class Shopping:
    cart = [] #class attribute,static attribute
    origin = 'china'

    def __init__(self, name, location):
        self.name = 'Siraggonj city' #instance attribute
        self.location = location
        
    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'buying: {item} for price: {price} and remaining: {remaining}')

    #static method
    @staticmethod
    def multiply(a, b):
        result= a*b
        print(result)

    @classmethod #static class method
    def hudai_dakhi(self, item):
        print('Huday dahi kinbo na', item)

    
basundhara = Shopping('Bashu', 'Dhaka Banani')
basundhara.purchase('Lungi', 500, 1000)
basundhara.hudai_dakhi('Lungi')
Shopping.hudai_dakhi('Saban')
Shopping.multiply(3,4)
basundhara.multiply(5,4)


         