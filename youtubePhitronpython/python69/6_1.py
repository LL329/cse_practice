# pb-1. Python program to print a multiplication table of a given number

table = int(input(f'Give a number to see multiplication table: '))
for i in range(1,11):
    print(table," X ", i, " = ", table*i)
    