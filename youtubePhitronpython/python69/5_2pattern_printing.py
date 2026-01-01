# pattern printing problem solving in python
# for row in range (7):
#     for col in range (row + 1):
#         print("#", end=" ")
#     print()

# while loop
row = 0
while row < 6:
    row += 1
    col = 0
    while col < row + 1:
        col += 1
        print("#", end=" ")
    print()