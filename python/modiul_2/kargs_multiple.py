def full_name(first,last):
    name = f'{first} {last}'
    return name
# print(full_name("John", "Doe"))
# name = full_name("John", "Doe")
name = full_name(last="Doe", first="John")
print('Full name is :',name)


def person_info(firs, last , **addition):
    name = f'{firs} {last}'
    # print(addition['title'])
    for key, value in addition.items():
        print(f'{key} : {value}')
    return name

info=person_info(firs="james", last="bond", title="agent", title2="shayok",age="34")
print(info)


def a_lot(num1,num2):
    sum = num1 + num2
    mul = num1 * num2
    div = num1 / num2
    remain = num1 % num2
    # return sum, mul, div, remain
    return[sum, mul, div, remain]
everything = a_lot(77,44)
print(everything)