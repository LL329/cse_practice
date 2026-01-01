# pb-> 1 : swaping two list elements

a = [17,12, 13, 15, 16, 10]
tmp = a[0]
a[0] = a[-1] # a[len(a)-1]
a[-1] = tmp

print(a)
