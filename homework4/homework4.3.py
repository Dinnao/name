A = int(input('Enter an int number: '))
B = int(input('Enter second int number: '))
some = A
New_list = []
steps = 0

while some != B:
    some += 1
    steps += 1
while steps != 0:
    New_list.append(A)
    A += 1
    steps -= 1
New_list.append(B)
print(New_list)
# elif A < B:
#     while B != some:
#         some -= 1
#         steps += 1
#     while steps != 0:
#         New_list.append(A)
#         A -= 1
#         steps -= 1
#     New_list.append(B)
