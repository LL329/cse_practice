# taking multiple inputs from user it in a list

# Problem - 1 : taking multiple string input

# a = input().split()
# print(a)

# Problem - 1 : taking multiple int input

# a = list(map(int, input(f'You can give int digits : ').split())) # map(ki korbo, kar opore apply korbo)
# print(a)

# Problem - 3 : taking multiple float input
# s = list(map(float, input(f'You have to give float digits : ').split()))
# print(s)


#map(function, iterable)
#function-> float , iterable->numbers
#first parameter everytime function & second parameter iterable

#Ex-1
# numbers = ["12.5", "19.3", "7.0"]
# result = list(map(float, numbers))
# print(result)


# Example 2
# words = ["phitron", "mango", "banana"]
# result = list(map(str.upper, words))
# print(result)

#Ex-3
# def square(x):
#     return x * x

# nums = [1, 2, 3, 4]
# result = list(map(square, nums))
# print(result)

# ....................lambda.............................

# 👉 এটা হলো একটা ছোট্ট function (যাকে আমরা lambda function বলি)।

# এখানে x মানে লিস্টের প্রতিটি element

# x+10 মানে প্রতিটি element‑এর সাথে 10 যোগ করা হবে

# 📌 উদাহরণ:

# যদি x = 1 → 1+10 = 11

# যদি x = 2 → 2+10 = 12

# যদি x = 3 → 3+10 = 13

# যদি x = 4 → 4+10 = 14
nums = [1 ,2 , 3, 4, 5]
rst = list(map(lambda x : x+10 , nums))
print(rst)

