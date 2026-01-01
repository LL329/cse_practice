import math
import time
def timer(func):
    def inner(*args, **kwargs):
        print('time start from hare')
        start = time.time()
        func(*args, **kwargs)        
        print('time end from hare')
        end = time.time()
        print(f'total time taken {end-start}')
    return inner
# timer()()

@timer
def get_factorial(n):
    print('factorial starting')
    result = math.factorial(n)
    print(f'factorial of {n} is : {result}')

get_factorial(n = 7)
