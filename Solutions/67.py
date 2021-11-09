import time

start = time.time()

import os

current_path = os.path.dirname(__file__)

new_path = os.path.relpath(
    '..\\Additional files\\67_triangle.txt', current_path)

triangle_file = open(new_path, 'r')

triangle_list = triangle_file.read().splitlines()

triangle = []

for row in range(len(triangle_list)):
    triangle.append(triangle_list[row].split())
    triangle[row] = [int(n) for n in triangle[row]]

for i in range(1, 100):
    triangle[i][0] += triangle[i - 1][0]
    triangle[i][i] += triangle[i - 1][i - 1]
    for j in range(1, i):
        triangle[i][j] += max(triangle[i - 1][j], triangle[i - 1][j - 1])

print(max(triangle[99]))

end = time.time()

# Executes in 0.00601 seconds
print(end - start)