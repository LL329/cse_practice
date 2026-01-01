numbers = [88,89,12,45,98,68]
numbers.append(70)
print(f'last elements is hand making',numbers)
numbers.insert(2,71)
print(numbers)
numbers.insert(0,12)
print(numbers)
numbers.remove(98)
print(numbers)

if 68 in numbers:
    numbers.remove(68)
    print(numbers)

    last = numbers.pop()
    print(last,numbers)

    index = numbers.index(12)
    print(index)

    if 7 in numbers:
     numbers.index(7)
    print(index)

    numbers.sort()
    print(numbers)

    numbers.reverse()
    print(numbers)