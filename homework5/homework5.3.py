def triange():
    a = int(input('Enter first side of triangle: '))
    b = int(input('Enter first side of triangle: '))
    c = int(input('Enter first side of triangle: '))
    p = (a + b + c)/3
    x = float((p * (p-a) * (p-b) * (p-c)))
    s1 = (x ** 0.5)
    print(s1)


def square():
    a = int(input('Enter first side of square: '))
    b = int(input('Enter second side of square: '))
    s = a * b
    print('S of square is: ' + str(s))

def chois():
    ch = input('Please enter figure, 1 - tiangle | 2 - square')
    if ch == '1':
        triange()
    elif ch == '2':
        square()
    else:
        triange()

chois()

