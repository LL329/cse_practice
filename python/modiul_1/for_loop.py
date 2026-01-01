numbers = [5,10,15,20,25]
sum = 0
for num in numbers:
    if num == 15:
        continue
    print(f'number is {num}')
    sum+=num
    if sum >= 20:
        print('Bigger value reached: ')
        break
    # print(sum)


print(f'The total sum is {sum}')


text = 'Hello world'
for char in text:
    if char =='o':
        continue
    if char=='r':
        break
    print(char)

    