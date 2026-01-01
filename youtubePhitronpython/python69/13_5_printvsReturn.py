# Print vs Returns in Function
# print is fixed and return will be mudify


#print korla modify kora jabe na
def sum(a,b):
    print(f'sum of {a} * {b} = {a*b}')
sum(2,3)

# return korla modify kora jabe
def sum_with_return(a,b):
    return a+b # return means to stopped
result=sum_with_return(2,3)
result += 4
print(result)
print(sum_with_return (25,3))
print(sum_with_return(2,3)*3)