# python program to check Armstrong Number
# a = int(input())
# num_len = len (str(a))
# tmp = a
# sum = 0
# while tmp > 0:
#     lst_digit = tmp % 10
#     sum = sum + lst_digit ** num_len
#     tmp //=10
# if sum == a:
#     print("Armstrong Number")
# else:
#     print("Not a Armstrong Number")


#shortcut
a = input()
num_len=len(a)
sum = 0
for i in a:
    sum +=int(i)**num_len
if int(a) == sum:
    print("Armstrong")
else:
    print("Not armstorng")