from random import randint

numbers = []
numbers_mask = []
for i in range(20):
    numbers.append(randint(0, 20))
for val in numbers:
    if val % 2 == 0:
        numbers_mask.append(val)
print(numbers)
print(numbers_mask)
#не понял как заменить нулями