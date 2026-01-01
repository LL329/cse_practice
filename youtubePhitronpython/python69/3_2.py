#pb2.take three integer input from user and find the largest number between using if-elis-else statement

num1 = int(input(f'First input : '))
num2 = int(input('Second input from user :'))
num3 = int(input(f'Third input from user : '))

if num1 >= num2 and num1 >= num3:
    print(f'Largest number is num ')
elif num2 >= num1 and num2 >= num3:
    print(f'Largest number is num2 ')
else :
    print(f'Largest number is num3 ')


# nsested if else 
# a = int (input())
# b = int (input())
# c = int (input())

# if a>=b:
#     if a>=c:
#         print(a, f'is the largest')

#     else: 
#         print(c, f'is the largest')

# else:
#     if b>= c:
#         print(b, f'is the largest')
#     else:
#         print(c, f'is the largest')
