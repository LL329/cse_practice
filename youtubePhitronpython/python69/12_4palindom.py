# checking palindom string
# input : "Madam" "amma" "tit"
# Output : "Yes"


a = input("Enter string : ")
if a == a[::-1]:
    print("Yes")
else:
    print("NOt")
