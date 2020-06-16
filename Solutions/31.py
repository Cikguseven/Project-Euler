'''
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
'''

import time

start = time.time()

count = 0

# Breaks down problem by calculating number of ways change can be given in smaller denominations. Does not consider 1p coins as they will be automatically added to fill up every way.
for a in range(3): # Possible number of £1 coins
	for b in range(1 + int((200 - 100 * a) / 50)): # Possible number of 50p coins
		for c in range(1 + int((200 - 100 * a - 50 * b) / 20)): # Possible number of 20p coins
			for d in range(1 + int((200 - 100 * a - 50 * b - 20 * c) / 10)): # Possible number of 10p coins
				for e in range(1 + int((200 - 100 * a - 50 * b - 20 * c - 10 * d) / 5)): # Possible number of 50p coins
					for f in range(1 + int((200 - 100 * a - 50 * b - 20 * c - 10 * d - 5 * e) / 2)): # Possible number of 2p coins
						count += 1
									
print(count + 1) # Total no. of ways + 1 way with 1 x £2 coin

end = time.time()

print(end - start) # Executed in 0.0110 seconds				

						