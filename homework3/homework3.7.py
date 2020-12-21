import numpy as np
i = int(input('Please enter an integer number: '))
new_list = []
step = 0

while step != i:
    step += 1
    new_list.append(step)

result = np.prod(np.array(new_list))
print(result)