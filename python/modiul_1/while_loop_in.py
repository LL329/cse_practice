num = 1
while num <20:
    if num%2 ==1:
            num+=1
            continue
    if num % 2 ==0:
        
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
    num+=1
    if num ==14:
        break
    