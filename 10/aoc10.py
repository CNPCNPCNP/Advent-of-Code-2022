from collections import deque

strengths = 0
x = 1

with open(r'10\input.txt') as input:
    ops = deque()
    for index, line in enumerate(input):
        line = line.strip().split(" ")
        print(line)
        if line[0] == "addx":
            ops.append(int(line[1]))
        else:
            ops.append(0)

executing = False
crt = [['.']*40 for i in range(6)]
print(crt)

for cycle in range(1, 240):
    if (cycle - 20) % 40 == 0:
        print(cycle, x)
        strengths += x * cycle
    if not executing and ops[0] == 0:
        ops.popleft()
        continue
    if not executing:
        executing = True
    else:
        executing = False
        x += ops.popleft()

x = 1
row = 0
executing = False

with open(r'10\test.txt') as input:
    ops = deque()
    for index, line in enumerate(input):
        line = line.strip().split(" ")
        print(line)
        if line[0] == "addx":
            ops.append(int(line[1]))
        else:
            ops.append(0)

for cycle in range(1, 241):
    drawing = cycle % 40
    if drawing == 0:
        drawing = 40
    if not ops:
        pass
    elif not executing and ops[0] == 0:
        ops.popleft()
    elif not executing:
        executing = True
    else:
        executing = False
        x += ops.popleft()
    
    col = drawing - 1
    if drawing % 40 == 1 and cycle != 1:
        row += 1 

    if drawing == x or drawing == x - 1 or drawing == x + 1:
        print(row, col)
        crt[row][col] = "#"
    
for line in crt:
    print("".join(line))
