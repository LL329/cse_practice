# simple problem solving strintg sorting
# alphabetically sorting


# res = res + a[i] * int(a[i+1])

# এখানে মূল ম্যাজিক।

# a[i] হলো অক্ষর।

# int(a[i+1]) হলো সংখ্যা।

# a[i] * int(a[i+1]) মানে হলো অক্ষরটাকে সংখ্যার বার রিপিট করা।

# উদাহরণ:

# x * 3 → xxx

# b * 4 → bbbb

# u * 5 → uuuuu

# i * 2 → ii

# সব মিলিয়ে res = "xxxbbbbuuuuuii"


#       ////////////////////////////////         #

# input : x3b4U5i2
# output: bbbbiiUUUUUxxx

a = input()
res = ""
for i in range(0,len(a),2):
    # res = res + a[i]
    print(f'{a[i]} {a[i+1]}')
    res = res + a[i] *int(a[i+1])
result = sorted(res , key=str.casefold)
res_string = "".join(result) # list to string
print(res_string)


