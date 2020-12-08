world = input()
new_list = world.split(' ')
num = []
len_of_num = len(num)
def count():
    nl_len = len(new_list)
    symb_len = len(new_list[0]) + len(new_list[len_of_num])
    print('Num of words is: ' + str(nl_len))
    print('Num of symbols is: ' + str(symb_len))
count()



