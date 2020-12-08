def Square(a):
    colors = {'Perimeter': 4 * a, 'Square': a * a, 'Diagonal': (2 ** 0.5)*a}
    print('Perimeter is: ' + str(colors['Perimeter']))
    print('Square is: ' + str(colors['Square']))
    print('Dioganal is: ' + str(colors['Diagonal']))
Square(4)