#factorial of a number in python
# 
user_input= int(input("Enter a Value : "))
factorial = 1
for i in range(1,user_input+1):
    factorial*=i
print(factorial)
