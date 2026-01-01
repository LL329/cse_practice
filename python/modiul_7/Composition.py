# ১. প্রথমে একটি Engine class তৈরি করছি
class Engine:
    def __init__(self):
        pass

    def start(self):
        print("engine started")  # ইঞ্জিন চালু করার method

class Driver:
    def __init__(self):
        pass

# ২. এবার Car class তৈরি করছি, যার মধ্যে Engine class-এর object থাকবে
class Car:
    def __init__(self):
        self.engine = Engine()  # Car-এর মধ্যে Engine object রাখা হচ্ছে

    def start_car(self):
        print("starting to run the car")
        self.engine.start()  # Car-এর মাধ্যমে Engine-এর method কল করা হচ্ছে
        self.driver = Driver()

    def start(self):
        self.engine.start()

# ৩. Car class-এর object তৈরি করে গাড়ি চালু করছি
my_car = Car()       # একটি Car object তৈরি
my_car.start_car()   # Output: গাড়ি চালু করার চেষ্টা করছি... ইঞ্জিন চালু হয়েছে
