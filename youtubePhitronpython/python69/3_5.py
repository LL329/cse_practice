#pb-5. Write a program to check whether is leap year or not.Take input from user. if year = 1996, it is leap year . conddition for leap year : 1. if a year divisible by both 400 and 100 it is a leap year . 2. if a year divisible by 4 and divisible by 100 it is a leap year


leapYearCheck = int(input(f' You can check leap year  hare : '))

if leapYearCheck % 400 == 0 and leapYearCheck % 100 == 0 :
    print(f'It is a leap year')
elif leapYearCheck % 4 == 0 and leapYearCheck % 100 != 0 :
    print(f'It is a leap year ')
else :
    print(f'It is not a leap year ')


#shortcut method
year = int(input(f'give me year :'))
if(year % 400==0 and year % 100==0) or (year % 4 == 0 and year % 100 != 0):
    print("leap Year")
else:
    print("Not leap Year ok")