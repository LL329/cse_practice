class Bank:
    def __init__(self, holder_name, initial_deposit):
        self.holder_name = holder_name
        self.balance = initial_deposit
    
rafsan = Bank('Choto bhay', 1000)
print(rafsan.holder_name)
print(rafsan.balance)