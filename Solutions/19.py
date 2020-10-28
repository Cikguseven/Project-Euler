import time

start = time.time()

from datetime import date

solution = 0

for year in range(1901, 2001):
    for month in range(1, 13):
        day = date(year, month, 1)
        if day.weekday() == 6:
            solution += 1

print(solution)

end = time.time()

# Executes in 0.00200 seconds
print(end - start)
