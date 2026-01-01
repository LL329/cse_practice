boss = True
if boss is not True:
    print('you are the boss')
else:
    print('you are not the boss')



# Nested condition
coin = 'head'
if boss == True:
    print('You are the best boss')
    if coin == 'head':
        print('You won the coin toss')
    elif coin == 'tail':
        print('You lost the coin toss')
        if 5>2 or 3<1:
            print('Youa are lucky')

else:
    print('You are not my boss')

