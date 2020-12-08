from datetime import date
d = int(input("Введите день"))
m = int(input("Введите месяц"))
y = int(input("Введите год"))
try:
    data = date(y, m, d)
    print(data)
    print("Дата существующая")
except:
    print("Такой даты нет")