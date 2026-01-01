# list builting in methods
# list() convert stirng to list
# append() adds an element at the end of the list
# inser() adds an element at the specificed position
# copy() Returns a copy of the list
#count() Returns the number of elements with the specified value
# extend() add the elements of a list to the end of the current list


# add two list 
# a = [1,2,3]
# b = [4,5,6]
# c = a + b
# print(c)


# to convert a sting in list
# s = "Hello World!"
# print(list(s))


# .append method to add value in last index
# a = [12,24,13,45]
# a.append(40) # dot dia method bujai
# print(a)


# .insert method to add value in any index
# a = [1,2,3,4,5]
# a.insert(2,100) # in which position i add and it's value
# print(a)


# #copy
# a = [1,2,3,4,5]
# b = a.copy() # or
# b = a # a assign value to b
# print(b)


# #count 
# a = [1,2,3,4,2, 22,2,5,'a','b','c','c','c']
# print(a.count(2))


# extend 
a = [12,2,5,6]
# a.extend([32,90]) / same way below
a = a + [32,90]
print(a)