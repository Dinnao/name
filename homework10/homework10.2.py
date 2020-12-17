def palindrom():
    string = input('Please input some string: ')
    r_string = string[::-1]
    print(string == r_string)

palindrom()