class Company:
    def __init__(self, name, address, ):
        self.name = name
        self.bus = []
        self.routes = []
        self.drivers = []        
        self.counter = []
        self.manager = []
        self.supervisors = []
        self.fare = []


class Driver:
    def __init__(self, name, license, age):
        self.license = license
        self.name = name
        self.age = age


class Counter:
    def __init__(self):

      pass
    def __purchase_a_ticket(self, start, destination):
        pass
  

class Passenger:
    pass


class Supervisors:
    pass

Mohabbot_driver = Driver('Rohim bokso', 23, 89)
print(Mohabbot_driver.name, Mohabbot_driver.age, Mohabbot_driver.license)


    