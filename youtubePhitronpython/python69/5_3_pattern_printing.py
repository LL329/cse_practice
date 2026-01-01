#ascii value a= 97,b=98,c=99,d=100,e=101,e=102,f=103
#ascii value A=65,B=66,C=67,D=68,E=69,F=70,G=71


for i in range (0,26,3):
    for j in range(i+1):
        print(chr(97+i) , end=" ")
    print()