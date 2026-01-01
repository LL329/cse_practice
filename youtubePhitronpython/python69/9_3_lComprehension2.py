# [Expresion (element) for element in list if condition]
# Example-4: using if with List Comprehension
# a = []
# for i in range(1,20):
#     if i % 3 == 0:
#         a.append(i)
# print(a)
        # list comprehension sort code same work
# s = [t for t in range(1,20) if t % 3 == 0]
# print(s)

#Example-5:Nested if with list Comprehension

# a = []
# for i in range(1,20):
#     if i % 3 == 0:
#         a.append(i)
#     if i% 5 == 0:
#         a.append(i)
# print(a)

# list comprehension 
# b = [i for i in range(1,20) if i % 3 == 0  or
#       i % 5 == 0]
# print(b)

#Example 6: if.........else with List Comprehensiion
#[if else for i in list]

# a = []
# for i in range(20):
#     if i % 2 == 0:
#         a.append("Even")
#     else:
#         a.append("Odd")
# print(a)

#comprehension .............
a = ["Even" if i%2 == 0 else "Odd" for i in range(20)]
print(a)