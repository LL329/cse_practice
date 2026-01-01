# [Expression for item in list]
# Example-1:Iteration with list comprehension
a = [10, 20, 30, 40, 50]
b = [i*10 for i in a] # multiply 10 times for every indexs
print(b)


# Example-2:Iterating through a string Using list comprehension
a= "Hello World!"
# b=[i for i in a] # transfer in list
b = list(a)
print(b)


# Example-3:Using range() function in list comprehension
a = [i for i in range(1,11,2)]
# a = list(range(2,11,2))
b = [i for i in range(2,11,2)]
print(b)
print(a)

