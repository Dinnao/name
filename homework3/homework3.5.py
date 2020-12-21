import random
i = random.randint(1, 10)
n = int(input('Please enter number from 1 to 10: '))
if i == n:
    print('You win! The number was: ' + str(i))
elif i != n:
    print('You lose! The number was: ' + str(i))
