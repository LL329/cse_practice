class shopping:
    def __init__(self,name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity' : quantity}
        self.cart.append(product)

    def remove_from_cart(self, item_name):
        for product in self.cart:
            if product['item'] == item_name:
                self.cart.remove(product)
                print(f"{item_name} removed from cart.")
                return
        print(f"{item_name} not found in cart.")

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            # print(item)
            total += item['price'] * item ['quantity']
        print('total price', total)
        if amount < total:
            print(f'please provide {total-amount} more')
        else:
            extra = amount - total
            print(f'Here is your items and extra money{extra}')


swapan = shopping('Alan shopan')
swapan.add_to_cart('alu', 50, 10)
swapan.add_to_cart('dim', 12, 1)
swapan.add_to_cart('rice', 50, 10)

swapan.remove_from_cart('alu')
swapan.remove_from_cart('begun')

print(swapan.cart)
swapan.checkout(500)