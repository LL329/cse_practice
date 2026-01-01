class Laptop:
    def __init__(self, brand, price, color, memory):
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory

    def run(self):
        return f'Running laptop: {self.brand}'   
    

    def coding(self):
        return f'Learning python and practicing'

class Phone:
    def __init__(self, brand, color, dual_sim):
        self.brand = brand
        self.color = color
        self.dual_sim = dual_sim

    def Phone_run(self):
        return f'scr phone every time: {self.Phone_call}'

    def Phone_call(self, number, text):
        return f'Sending SMS to: {number} with: {text}'   
    

class Camera:
    def __init__(self, brand, price, color, pixel):
        self.brand =brand
        self.price = price
        self.color = color
        self.pixel = pixel


    def run(self):
        pass

    def change_lens(self):
        pass
        