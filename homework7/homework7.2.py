steps = []
def step(Cel):
    while Cel != 0:
        steps.append(1)
        Cel -= 1
step(int(input('Please enter Celsius: ')))
def calculate_far(Cel):
    Cel = len(steps)
    Far = Cel * 1.8 + 32
    print('In fahrenheit: ' + str(Far))
def calculate_kel(Cel):
   Cel = len(steps)
   Kel = Cel + 273.15
   print('In kelvins: ' + str(Kel))
calculate_far(1)
calculate_kel(1)