some_numb = [int(input('Enter any numbers. 0 = end: '))]
numb_of_some_numb = len(some_numb)
print(some_numb)
while 0 not in some_numb:
   some_numb.append(int(input()))
   print(some_numb)
some_numb.remove(0)
print('len of numbers is: ' + str(len(some_numb)))
print('Sum of numbers is: ' + str(sum(some_numb)))
print(sum(some_numb)/len(some_numb))
max_digit = 0
num_mult = 1
num_count_1 = 0
num_count_2 = 0
for i, value in enumerate(some_numb):
   num_mult *= value
   if value > max_digit:
       max_digit = value
       max_digit_index = i
   if i % 2 == 0:
       num_count_2 += 1
   elif i % 2 != 0:
       num_count_1 += 1
print(num_mult)
print(num_count_2)
print(num_count_1)
print(max_digit, max_digit_index)