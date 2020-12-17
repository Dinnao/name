file = open('new_file', 'w')
while True:
    arg = input("Please, enter some string. End - '': ")
    if arg == '':
        break
    file.write(arg+'\n')

