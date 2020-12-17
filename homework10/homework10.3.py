def go_list(arg, some_list):
    some_list = some_list[arg:] + some_list[:arg]
    print(some_list)
go_list(3, [1, 2, 3, 4, 5, 6, 7, 8, 9])