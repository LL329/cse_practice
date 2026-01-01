# def doubled(x):
#     return x*2

# result = doubled(33)
# print(result)

# squared = lambda x ,y:x+y
# sum = squared(11,33)
# print(sum)

# twice = lambda x : x*2
# tresult=twice(2)
# print(tresult)


# rut=lambda x,y : x**y
# sqr=rut(16,4)
# print(sqr)

# numbers = [12,56,98,78,56,12,6,98]
# # doubled_numbs = map(doubled,numbers)
# # doubled_numbs=map(lambda x : x*2,numbers)
# doubled_numbs=map(lambda x:x*x,numbers)
# print(numbers)
# print(list(doubled_numbs))




actors = [
    {'name' : 'sabana', 'age': 30},
    {'name' : 'sabnor', 'age':44 },
    {'name' : 'sabnas', 'age':21 },
    {'name' : 'moyore', 'age':15 },
    {'name' : 'julakha', 'age':49},
    ]

# junior = filter(lambda actors : actors['age'] < 33,actors)
# print(list(junior))
fivers = filter(lambda actors : actors['age']%5==0,actors)
print(list(fivers))