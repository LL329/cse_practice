balance = 3000
def buy_things(item, price):
    global balance 
    print(f'balance inside the funciton',balance)
    balance = balance-price

buy_things('phone', 1000)
print(balance)
