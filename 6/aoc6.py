# 1 user command
# 2 other thing

with open(r'6\input.txt') as input:
    tree = {"/": {"size": 0, "children": [], "parent": ""}}
    current = "/"
    reading = False
    size = 0
    for index, line in enumerate(input):
        if index == 0:
            continue
        line = line.strip()
        line = line.split(" ")

        if line[0] == "$":
            if reading:
                tree[current]["size"] = size
            if line[1] == "cd":
                reading = False
                _, _, target = line
                if target == "..":
                    current = tree[current]['parent']
                elif current == "/":
                    prev = current
                    current = '/' + target
                    tree[current] = {'size': 0, 'children': [], 'parent': prev}
                    tree[prev]['children'].append(current)
                else:
                    prev = current
                    current = current + '/' + target
                    tree[current] = {'size': 0, 'children': [], 'parent': prev}
                    tree[prev]['children'].append(current)

            if line[1] == "ls":
                reading = True
                size = 0

        if reading:
            if line[0].isdigit():
                size += int(line[0])

print(tree)

def get_size(dir):
    size = tree[dir]['size']
    for child in tree[dir]['children']:
        size += get_size(child)
    return size

overall = get_size("/")
print(overall)

total = 0
for dir in tree:
    if get_size(dir) <= 100000:
        total += get_size(dir)

print(total)

spare = 70000000 - overall
print(spare)

min_delete = 30000000 - spare
print(min_delete)

res = 'aishdirjjiartrae'
smallest = 49945849584954958
for dir in tree:
    size = get_size(dir)
    if size >= min_delete and size < smallest:
        res = dir
        smallest = min(smallest, size)

print(smallest)