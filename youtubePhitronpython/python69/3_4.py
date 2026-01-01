#pb-4 Write a problem to take input from user and display the grade according to the following criteria.

marks = int(input(f'Your Marks please : '))

if marks > 90 and marks <= 100:
    print(f'Your grade is : A ')
elif marks > 80 and  marks <= 90:
    print(f'Your grade is : B')
elif marks >= 60 and marks <= 80:
    print(f'Your grade is : C')
elif marks < 60 and marks >=33:
    print(f'Your grade is : D')
elif marks < 33:
    print(f'You have Fail try next year ')
else:
    print(f'Invalid marks ')