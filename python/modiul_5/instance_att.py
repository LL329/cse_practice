class shop:
    shopping_mall= 'Jamuna'
    def __init__(self,buyer): #constructor
        self.buyer = buyer
        self.cart = [] # cart is an instance attribute
     
    def add_to_cart(self,item):
        self.cart.append (item)

mehjabin = shop('mehjabin') 
mehjabin.add_to_cart('shoes')
mehjabin.add_to_cart('toilet cleaner')
mehjabin.add_to_cart('harfik')
print(mehjabin.cart)

nisho = shop('nisho')
nisho.add_to_cart('watch')
nisho.add_to_cart('tablet')
nisho.add_to_cart('medicine')
print(nisho.cart)

apurbo = shop('apurbo')
apurbo.add_to_cart('also a actor')
apurbo.add_to_cart('mouse')
apurbo.add_to_cart('saban')
print(apurbo.cart)