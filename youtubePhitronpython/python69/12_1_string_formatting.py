# More About String in Python
# Today's Topic : String formatting
# Method 1:
#formate function
name = "Rohim"
age = 20
# tmp_string = "I am {}. I am {} years old.".format(name,age)
# tmp_string = "I am {1}. I am {0} years old.".format(age,name)
tmp_string = "I am {fname}. I am {user_age} years old.".format(fname="karim",user_age=99)



print(tmp_string)

#Method 2:

#fstring
name = "Rahim"
age = 20
string = f'I am {name}. I am {age} years old'
print(string)