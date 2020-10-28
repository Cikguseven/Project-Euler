import time

start = time.time()

# Use of inflect module to convert number to words
import inflect

counter = 0

p = inflect.engine()

for i in range(1, 1001):
    counter += len(p.number_to_words(i).replace("-", "").replace(" ", ""))

print(counter)

end = time.time()

# Executes in 0.725 seconds
print(end - start)
