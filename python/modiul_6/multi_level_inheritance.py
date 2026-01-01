class Vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price


    def __repr__(self, name, price):
        self.name = name
        self.price = price
        
    def move(self):
        pass


class Bus(Vehicle):
    def __init__(self, name, price, seat):
        self.seat = seat
        super().__init__(name, price)


    def __repr__(self):
        return super().__repr__()
    


class Truck(Vehicle):
    def __init__(self, name, price, weight):
        self.weight = weight
        super().__init__(name, price)


    def __repr__(self):
        return super().__repr__()


class Pickup_Truck(Truck):
    def __init__(self, name, price, weight):
        super().__init__(name, price, weight)


    def __repr__(self):
        return super().__repr__()



class ACBus(Bus):
    def __init__(self, name, price, seat, temperature):
        self.temperature = temperature
        super().__init__(name, price, seat)


    def __repr__(self):
        return super().__repr__()


Green_Bus = ACBus('Green', 7790000, 200, 16)
print(Green_Bus)

