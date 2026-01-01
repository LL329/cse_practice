for i in range(1,10):
    if i%2 == 0:
        continue
    print(f'{i} is odd')

    sum = 0

    for num in range(1,11):
        sum +=num
        if sum==21:
            continue
        if sum>=30:
            print('large sum reached')
            break
        print(f'current sum is {sum}')