w = input('Enter some string: ')
def fstr_tolst(func):
    def wrapper():
        func()
        some = w.split(' ')
        return some
    return wrapper()



@fstr_tolst
def word():
    print(w)


