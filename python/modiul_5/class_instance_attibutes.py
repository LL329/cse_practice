class shop:
    cart = [] # cart is an class attribute
    def __init__(self,buyer): #constructor
        self.buyer= buyer

    def add_to_cart(self,item): #item add in cart 
        self.cart.append(item)


mahjabin = shop('meh jabeen')
mahjabin.add_to_cart('shoes')
mahjabin.add_to_cart('phone')
print(mahjabin.cart)


nisho=shop('nisho')
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')
print(nisho.cart)