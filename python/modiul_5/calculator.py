class Calculator:
    brand = 'casio99'  

    def __init__(self, num1, num2):  
        self.num1 = num1
        self.num2 = num2

    def add(self):  
        return self.num1 + self.num2

    def sub(self): 
        return self.num1 - self.num2

    def mul(self): 
        return self.num1 * self.num2
    
    def div(self):
        return self.num1 / self.num2

    def reminder(self):
        return self.num1 % self.num2

# অবজেক্ট তৈরি
result = Calculator(7, 2)
print("add =", result.add())  
print("sub =", result.sub())  
print("mul =", result.mul()) 
print('div = ', result.div())
print('reminder=',result.reminder()) 
