new_dict = {}
def comb_dict(keys, values):
    for k, v in zip(keys, values):
        new_dict[k] = v
comb_dict(keys=['Bitcoin', 'Ether', 'Ripple', 'Litecoin'] , values=['BTC', 'ETH', 'XRP', 'LTC'])
print(new_dict)

import datetime
import time
def count_doun(M):
    M = time.sleep(3)
count_doun(3)
def time_now(now):
    now = datetime.datetime.now()
    return print(now)
time_now(datetime.datetime.now())

new_dict = {}
new_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
key_list = []
len_of_list = len(new_list)
step = 0
while step != len_of_list:
   key_list.append(step)
   step +=1
def comb_dict(keys, values):
    for k, v in zip(keys, values):
        new_dict[k] = v
comb_dict(keys=key_list, values= new_list)
print(new_dict)