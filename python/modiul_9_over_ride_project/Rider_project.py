from abc import ABC, abstractmethod
from datetime import datetime


class Ride_sharing:
    def __init__(self, company_name):
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []

    def add_rider(self, rider):
        self.riders.append(rider)

    def add_driver(self, driver):
        self.drivers.append(driver)

    def __repr__(self):
        return f'{self.company_name} with riders: {len(self.riders)} and drivers: {len(self.drivers)}'


class User(ABC):
    id_counter = 1  # ✅ dynamic user ID

    def __init__(self, name, email, nid):
        self.name = name
        self.email = email
        self.__id = User.id_counter
        User.id_counter += 1
        self.wallet = 0
        self.__nid = nid

    @abstractmethod
    def display_profile(self):
        pass


class Rider(User):
    def __init__(self, name, email, nid, current_location, initial_amount):
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.current_ride = None
        self.wallet = initial_amount

    def display_profile(self):
        print(f'Rider: {self.name}, Email: {self.email}, Wallet: {self.wallet}')

    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount

    def update_location(self, current_location):
        self.current_location = current_location

    def request_ride(self, destination, ride_matcher):
        if not self.current_ride:
            ride_request = Ride_Request(self, destination)
            self.current_ride = ride_matcher.find_driver(ride_request)
            if self.current_ride:
                print(f'Ride started from {self.current_location} to {destination}')
            else:
                print('No driver available')


class Driver(User):
    def __init__(self, name, email, nid, current_location):
        super().__init__(name, email, nid)
        self.current_location = current_location

    def display_profile(self):
        print(f'Driver: {self.name}, Email: {self.email}, Wallet: {self.wallet}')

    def accept_ride(self, ride):
        ride.set_driver(self)


class Ride:
    def __init__(self, start_location, end_location):
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = 100  # ✅ fixed fare for simplicity

    def set_driver(self, driver):
        self.driver = driver

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self, rider):
        self.end_time = datetime.now()
        self.rider = rider
        if rider.wallet >= self.estimated_fare:
            rider.wallet -= self.estimated_fare
            self.driver.wallet += self.estimated_fare
            print(f'Ride ended. Fare: {self.estimated_fare}')
        else:
            print('Insufficient balance')


class Ride_Request:
    def __init__(self, rider, end_location):
        self.rider = rider
        self.end_location = end_location


class Ride_Matching:
    def __init__(self, drivers):
        self.available_drivers = drivers

    def find_driver(self, ride_request):
        if self.available_drivers:
            driver = self.available_drivers[0]
            ride = Ride(ride_request.rider.current_location, ride_request.end_location)
            ride.rider = ride_request.rider
            driver.accept_ride(ride)
            ride.start_ride()
            return ride
        return None


class Vehicle(ABC):
    speed = {
        'car': 50,
        'bike': 60,
        'cng': 15
    }

    def __init__(self, vehicle_type, license, rate):
        self.vehicle_type = vehicle_type
        self.license_plate = license
        self.rate = rate

    @abstractmethod
    def start_driver(self):
        pass


class Car(Vehicle):
    def start_driver(self):
        self.status = 'unavailable'


class Bike(Vehicle):
    def start_driver(self):
        self.status = 'unavailable'


# ✅ Testing the system
niya_jao = Ride_sharing('Niya Jao')
shakib = Rider('Shakib Khan', 'shakib@gmail.com', 1234, 'Bogra', 1200)
niya_jao.add_rider(shakib)
kala_pakhi = Driver('Kala Pakhi', 'kalahorin@gmail.com', 1238, 'Mirpur')
niya_jao.add_driver(kala_pakhi)

ride_matcher = Ride_Matching(niya_jao.drivers)
shakib.request_ride('Banani', ride_matcher)

print(niya_jao)
shakib.display_profile()
kala_pakhi.display_profile()
