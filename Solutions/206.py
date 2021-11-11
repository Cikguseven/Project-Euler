import time

start = time.time()

from math import ceil, floor, sqrt

valid = "1_2_3_4_5_6_7_8_9"

lower_bound = ceil(sqrt(int(valid.replace("_", "0"))))

upper_bound = floor(sqrt(int(valid.replace("_", "9"))))

for n in range(lower_bound, upper_bound + 1):
    if str(n)[-1] == "3" or str(n)[-1] == "7":
        x = str(n ** 2)
        if x[14] == "8":
            if x[12] == "7":
                if x[10] == "6":
                    if x[8] == "5":
                        if x[6] == "4":
                            if x[4] == "3":
                                if x[2] == "2":
                                    print(n)
                                    break


end = time.time()

# Executes in 17.2 seconds
print(end - start)
