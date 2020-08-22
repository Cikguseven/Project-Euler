import time

start = time.time()

from math import floor, log2

'''
# First solution
def dec_to_bin(dec_input):
    clone = dec_input
    new_bin = 0
    bin_length = int(floor(log2(dec_input)))
    for i in range(bin_length + 1):
        if dec_input % 2 == 0:
            dec_input /= 2
        elif dec_input % 2 == 1:
            new_bin += 1 * (10 ** i)
            dec_input = (dec_input - 1) / 2
    print(f'{clone} | {new_bin}')


for i in range(2, 10001):
    dec_to_bin(i)
'''

# Second solution (recursive)
def dec_to_bin(x):
    global temp
    if x > 1:
        dec_to_bin(x // 2)
        temp.append(str(x % 2))


for i in range(2, 10001):
    temp = ['1']
    dec_to_bin(i)
    print(f'{i} | {"".join(temp)}')

end = time.time()

print(end - start)
