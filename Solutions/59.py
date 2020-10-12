import time

start = time.time()

import os

current_path = os.path.dirname(__file__)

new_path = os.path.relpath('..\\Additional files\\59_cipher.txt', current_path)

cipher_text = open(new_path, 'r')

raw_text = cipher_text.read().split(',')

list_of_int = [int(n) for n in raw_text]

every_first_item = []

every_second_item = []

every_third_item = []

for a in list_of_int[0::3]:
    every_first_item.append(a)

for b in list_of_int[1::3]:
    every_second_item.append(b)

for c in list_of_int[2::3]:
    every_third_item.append(c)

print(set(every_first_item))





