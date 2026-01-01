class Gadget:
    def __init__(self, brand, price, color, origin):
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    def run(self):
        return f'Running laptop: {self.brand}'       

class Laptop:
    def __init__(self, memory, ssd):
        self.ssd = ssd
        self.memory = memory


    def coding(self):
        return f'Learning python and practicing'

class Phone:
    def __init__(self, dual_sim):
        self.dual_sim = dual_sim

    def Phone_run(self):
        return f'scr phone every time: {self.Phone_call}'

    def Phone_call(self, number, text):
        return f'Sending SMS to: {number} with: {text}'   
    def __repr__(self):
        return f'you have dual sim in your phone {self.dual_sim}'
    

class Camera:
    def __init__(self, brand, price, color, pixel):
        self.pixel = pixel


    def run(self):
        pass

    def change_lens(self):
        pass
        

my_phone = Phone(True)
my_phone.Phone_call() 
print(my_phone)