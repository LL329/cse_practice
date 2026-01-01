# string reversing
# input : "I love coding using Python"
# output : "I evol gnidoc gnisu nohtyp"

a = input("")
a = a.split(" ") # string k list ee convert 
print(a)
result = "" # reverse korer jonno string use kore
for i in a:
    result += i[::-1] + " " # string er man update hoscha
print(result)