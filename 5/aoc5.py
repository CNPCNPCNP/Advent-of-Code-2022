with open("5\input.txt") as input:
    reading = False
    stacks = [['F','C','J','P','H','T','W'],
              ['G','R','V','F','Z','J','B','H'],
              ['H','P','T','R'],
              ['Z','S','N','P','H','T'],
              ['N','V','F','Z','H','J','C','D'],
              ['P','M','G','F','W','D','Z'],
              ['M','V','Z','W','S','J','D','P'],
              ['N','D','S'],
              ['D','Z','S','F','M']]

    for line in input:
        line = line.strip()
        if reading:
            line = line.split(" ")
            cnt = int(line[1])
            colfrm = int(line[3]) - 1
            colto = int(line[5]) - 1
            tmp = []
            while cnt > 0:
                tmp.append(stacks[colfrm].pop())
                cnt -= 1
            
            for _ in range(len(tmp)):
                stacks[colto].append(tmp.pop())

        if line == "":
            reading = True

res = ""
for stack in stacks:
    res += stack[-1]
print(res)