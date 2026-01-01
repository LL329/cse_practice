# and , or , not -> work with boolean value
# left and right -> true hola = true returning
# lef or right -> 1 ta true holai = true hobe
# true k false , false k true kore not operator

#example of and
print("logical and = " , 10-4==6 and 10-5==15)
print("logical and  = " ,10-4==6 and 10-5==5)

#example of or
print("logical or = " , 10-4==6 or 10-15==15)
print("logical or = " ,10-4==6 or 10-5==5)


#example of not
print(f'logical operator not = ' ,not (10 - 4 == 6)) # true k false korlo
print(f'logical operator not = ' ,not (10 - 6 == 6)) #false k true korlo


marks = 89

if marks >= 90 and marks <=100:
    print("You can win two box of cocolate ")
elif marks >= 80 and marks < 90:
    print("You have chnage to win 1 box of cocolate")
else:
    print("You can't win any cocolate box yet ")
