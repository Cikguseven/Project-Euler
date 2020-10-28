import time

start = time.time()

import os

current_path = os.path.dirname(__file__)

new_path = os.path.relpath('..\\Additional files\\59_cipher.txt', current_path)

cipher_text = open(new_path, 'r')

raw_text = cipher_text.read().split(',')

cipher_list = [int(n) for n in raw_text]

decrypted_list = []

every_first_item = []

every_second_item = []

every_third_item = []

for a in cipher_list[0::3]:
    every_first_item.append(a)

for b in cipher_list[1::3]:
    every_second_item.append(b)

for c in cipher_list[2::3]:
    every_third_item.append(c)

every_first_ch = [a ^ 101 for a in every_first_item]

every_second_ch = [b ^ 120 for b in every_second_item]

every_third_ch = [c ^ 112 for c in every_third_item]

for a, b, c in zip(every_first_ch, every_second_ch, every_third_ch):
    decrypted_list.extend((a, b, c))

print(sum(decrypted_list))

end = time.time()

# Executes in 0.00200 seconds
print(end - start)
