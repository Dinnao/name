x = int(input('Enter start km: '))
y = int(input('Enter end km: '))
day = 0
some = x / 10
while x != y:
   x += some
   day += 1
   print(day)