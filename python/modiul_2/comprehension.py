numbers = [45,87,65,43,85,14,26,61]
odds=[]
numbers.sort()
print(sorted)
# numbers.reverse()
# print(numbers)
for num in numbers:
    if num % 2 == 1 and num % 3 == 0:
        odds.append(num)
print(odds)



players  = ['sakib','musfik','mustfiz']
ages = [38,37,32]

for player in players:
    print('player:',player)
