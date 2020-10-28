import time

start = time.time()

solution = 0

# Breaks down problem by calculating number of ways change can be given in
# smaller denominations starting from 1 pound. Does not consider 1p coins as
# they will be automatically added to fill up in every way.
for a in range(3):
    for b in range(1 + int((200 - 100 * a) / 50)):
        for c in range(1 + int((200 - 100 * a - 50 * b) / 20)):
            for d in range(1 + int((200 - 100 * a - 50 * b - 20 * c) / 10)):
                for e in range(1 + int((200 - 100 * a - 50 * b - 20 * c - 10
                                        * d) / 5)):
                    for f in range(1 + int((200 - 100 * a - 50 * b - 20 * c
                                            - 10 * d - 5 * e) / 2)):
                        solution += 1

print(solution + 1)

end = time.time()

# Executes in 0.0110 seconds
print(end - start)
