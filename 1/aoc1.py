first, second, third = 0, 0, 0
current = 0

with open("input1.txt") as file:
    for line in file:
        line = line.strip()
        if line == '':
            if current >= first:
                first, second, third = current, first, second
            elif current >= second:
                second, third = current, second
            elif current >= third:
                third = current
            current = 0
        else:
            current += int(line)

print(first + second + third)

