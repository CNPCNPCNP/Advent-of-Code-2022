import functools

pairs = []

with open(r'14\input.txt') as input:
    for index, line in enumerate(input):
        line = line.strip()
        if index % 3 == 0:
            left = eval(line)
        if index % 3 == 1:
            right = eval(line)
        if index % 3 == 2:
            pairs.append((left, right))

def compare(left, right):
    if right and not left:
        return 1
    if left and not right:
        return -1
    if not left and not right:
        return 0
    if type(left) == int and type(right) == int:
        if left < right:
            return 1
        if left > right:
            return -1
        if left == right:
            return 0
    if type(left) == list and type(right) == list:
        for x, y in zip(left, right):
            val = compare(x, y)
            if val == 1:
                return 1
            if val == 0:
                continue
            if val == -1:
                return -1
        if len(left) < len(right):
            return 1
        if len(left) == len(right):
            return 0
        if len(left) > len(right):
            return -1
    if type(left) == int and type(right) == list:
        return compare([left], right)
    if type(left) == list and type(right) == int:
        return compare(left, [right])

    
good_pairs = []
all_packets = []
all_packets.append([[2]])
all_packets.append([[6]])

first = [[2]]
second = [[6]]

for index, pair in enumerate(pairs):
    print(f'Pair: {pair}')
    left, right = pair
    if compare(left, right) == 1:
        good_pairs.append(index + 1)
    all_packets.append(left)
    all_packets.append(right)

res = []

all_packets.sort(key=functools.cmp_to_key(compare), reverse=True)
for index, packet in enumerate(all_packets):
    print(packet)
    if packet == first:
        res.append(index + 1)
    if packet == second:
        res.append(index + 1)

print(res)
print(res[0] * res[1])


