class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 10000

    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance+= amount

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            return f'You can\'t withdraw {self.min_withdraw}'

        elif amount > self.max_withdraw:
            return f'You can\'t withdraw more than 10thousands {self.max_withdraw}'
 

        else:
            self.balance -=amount
            return f'Here is your money {amount}'
        

brac = Bank(15000)
brac.withdraw(24)
brac.withdraw(25000)
print(brac.get_balance())

dbbl = Bank(5000)
dbbl.deposit(2000)
dbbl.deposit(1000)
print(dbbl.get_balance())
    

    