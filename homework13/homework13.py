from random import randint
class street:
    def __init__(self):
        self.houses = []
        for i in range(randint(5, 20)):
            self.houses.append((i, house()))

    def s_print(self):
        for house in self.houses:
            print('House№ ', house[0])
            house[1].h_print()


class house:
    def __init__(self):
        self.population = randint(1, 100)
    def h_print(self):
        print('Population is: ' + str(self.population))

class city:
    def __init__(self, c_name):
        self.c_name = c_name
        self.streets = []
        for i in range(randint(1, 5)):
            self.streets.append((i, street()))
    def c_print(self):
        print(self.c_name)
        for street in self.streets:
            print('Street №: ', street[0])
            street[1].s_print()

City = city('New York')
City.c_print()