#Indexing--> positive indexing st=0 1 2 3 4.... , negative indexing st=-1,-2,-3,-4.....


# a = [12, 20, 34, "Phitron"]
# print(a[0])
# a[-3] = 500
# print(a)
# if 20 in a:
#     print("found")
# else:
#     print("not found")


#     #traversing
# for i in range (len(a)):
#     print(a[i])


    #negative indexing to reverse
# a = [12, 20, 34, "Phitron"]
# for i in range (-1,-len(a)-1, -1): #st= -1, end = -len(a)-1, step = -1 kora komba
#     print(a[i])

# for i in range(len(a)-1, -1,-1):
#     print(a[i])


#........................Recap st...............

a = [12, 20, 34, "phitron"]
# print(a[0])
# print(a[-1])
# print(len(a))
# a[-3] = 500
# print(a)
# if 20 in a:
#     print("found")
# else:
#     print("not found")

#traversing.................
# for i in a:
#     print(i)

# for i in range(len(a)):
#     print(a[i])

#negative indexing .............
# for i in range(len(a)-1,-1,-1):
#     print(a[i])

# for i in range(-1, -len(a)-1,-1):
#     print(a[i])



#nested list...........
b = [[12 ,13], [18,23,"Phitron"],[-1,-19]]
print(b[2][1])
b[0][1]=99
print(b[0])