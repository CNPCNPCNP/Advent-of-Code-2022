from heapq import *

field = []

with open(r'12\test.txt') as input:
    for index, line in enumerate(input):
        line = line.strip()
        field.append([ord(x) - ord('a') for x in line])

print(field)

for row, _ in enumerate(field):
    for col, value in enumerate(_):
        if value == -14:
            start = (row, col)
            field[row][col] = 0
            print(row, col)
        if value == -28:
            finish = (row, col)
            field[row][col] = 26
            print(row, col)
