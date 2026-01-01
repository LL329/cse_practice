# pbl-> 2: count unique elements in an list
# never can be double
# 

a = [1, 2, 2, 3, 4, 4, 4, 5, 6]
b = []
count = 0
for i in a:
    if i not in b:
        count+=1
        b.append(i)

print(count)