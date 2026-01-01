#reversing a number using python
# int number reverse

a = int(input())
rev_a = 0
while a>0:
    last_digit = a % 10
    rev_a = rev_a*10 + last_digit  
    a //= 10
print(rev_a)