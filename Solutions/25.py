'''
The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''

import time

start = time.time() 

a = 1 

b = 1

index = 2

x = 10 ** 999 # Smallest 1000 digit number

while True: # Generate Fibonacci numbers and stops if number reaches length of 1000
    a = a + b
    index += 1
    if a >= x:
        break
    b = a + b
    index += 1
    if b >= x:
        break

print(index) # Prints index of first term with 1000 digits

end = time.time()

print(end - start) # Executes in 0.00400 seconds