# list method 2
# pop() removes and returns the last value from the list or given index value.
# remove() Removes a given  objects from the list
# clear() remove all items from the list
# sort() Sort a list in acending , decending
# max() Calculates maximum fo all the element of list
#reverse() REverse objects of the list in place.



# # pop() methods delete last element
# a = [1,2,3,4,5]
# print(a.pop()) # see which element is deleting
# print(a)

# remove () methods particular index remove
# a = [1,2,3,4,5]
# a.remove(2) #  remove index name 2
# print(a)


#clear() remove full index
# a = [1,2,3,4,5]
# a.clear()
# print(a)

# reverse() 
# a = [1,2,3,4,5]
# print(a[::-1]) same function below
# a.reverse()
# print(a)


#sort-> acending order 1 2 3 4
#sort-> decending order 4 3 2 1
# a = [32,22,4,3,1,7,11,40]
# a.sort() #acending order sort , by default false 
# print(a)
# a.sort(reverse=True) #decending order sort
# print(a)


# max() Calculates maximum fo all the element of list
a = [1, 200, 3, 82,22,4,3,1,7,11,40]
print(max(a)) # maximum of the list
print(min(a)) # minimum of the list