def sum(num1,  num2):
    add = num1 + num2
    return add
total = sum(10, 20)
print('The sum is:',total)


def all_sum(num1, num2 ,*numbers):
    print('Numbers',numbers)
    sum = 0
    for num in numbers:
        sum+=num
    return sum


total = all_sum(10,20,30,50,70,90,100)
print('The sum is :',total)


def do_a_lot (*args):
    print('Arguments are:',args)
check_ag=do_a_lot(10,20,30,40,50,60,70,80,90,100)
