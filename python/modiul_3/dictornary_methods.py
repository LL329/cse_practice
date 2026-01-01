numbers=[12,56,98,78,12,26,12,98]
person = {'name': 'kalachan pakhi', 'address': 'kaliyakor', 'age': 23, 'job': 'facebooker'}
# print(person)
# print(person.keys())
# print(person.values())
# print(person['address'])
# person['language']='Javascript'
# print(person)
# del person['name']
# print(person)
person['name']='Luckey Man'
print(person)

for key,value in person.items():
    print(key, value)

# person2={'Nam': 'Johir vaggoban', 'Age':22,'Address': 'corpara','Job': 'Facebooker'}
# print(person2)
# # print(person2.values)
# # print(person2.keys)
# # print(person2['Address'])
# # person2['language']='python'
# person2['Nam']='Luckey person'
# print(person2)
# # del person2['Age']
# # print(person2)



my_dict = {'a': 1, 'b': 2}
my_dict['c'] = 3  # Assign a new key-value pair
my_dict['a'] = 10  # Update an existing key
print(my_dict)  # Output: {'a': 10, 'b': 2, 'c': 3}

my_dict = {'a': 1, 'b': 2}
my_dict.update({'b': 20, 'c': 30})  # Update 'b' and add 'c'
print(my_dict)  # Output: {'a': 1, 'b': 20, 'c': 30}
#3. Using setdefault()
#The setdefault() method assigns a value to a key only if the key does not already exist.

#Python

#Copy code
my_dict = {'a': 1, 'b': 2}
my_dict.setdefault('c', 3)  # Adds 'c' with value 3
my_dict.setdefault('a', 10)  # Does nothing since 'a' exists
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}
#These methods provide flexibility for assigning or updating dictionary values depending on your needs.

