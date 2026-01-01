# ১. একটি base class তৈরি করছি Animal নামে
class Animal:
    def __init__(self, name):
        self.name = name  # name attribute সংরক্ষণ করা হচ্ছে

    def speak(self):
        print(f"{self.name} শব্দ করছে")  # speak() method: নামসহ একটি বার্তা প্রিন্ট করে


# ২. Dog নামে একটি subclass তৈরি করছি, যা Animal class থেকে উত্তরাধিকার পায়
class Dog(Animal):
    def speak(self):
        print(f"{self.name} ঘেউ ঘেউ করছে")  # speak() method override করে নতুন বার্তা দেয়

# ৩. Dog class-এর একটি object তৈরি করছি
my_dog = Dog("Tommy")  # Tommy নামের একটি Dog object তৈরি

# ৪. speak() method কল করছি
my_dog.speak()  # Output: Tommy ঘেউ ঘেউ করছে
                               