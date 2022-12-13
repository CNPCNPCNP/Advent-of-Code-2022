monkeys = []

with open(r'11\input.txt') as input:
    for index, line in enumerate(input):
        line = line.strip()
        if index % 7 == 0:
            monkey = {'number': index // 7, 'items': [], 'inspections': 0}
        if index % 7 == 1:
            line = line.replace(",", "")
            line = [int(num) for num in line.split()[2:]]
            for item in line:
                monkey['items'].append(item)
        if index % 7 == 2:
            line = line.split()[4:]
            monkey['operation'] = line
        if index % 7 == 3:
            line = line.split()[3:]
            divisor = int(line[0])
            monkey['divisor'] = divisor
        if index % 7 == 4:
            line = line.split()[5:]
            true_monkey = int(line[0])
            monkey['true'] = true_monkey
        if index % 7 == 5:
            line = line.split()[5:]
            false_monkey = int(line[0])
            monkey['false'] = false_monkey
        if index % 7 == 6:
            monkeys.append(monkey)

monkeys.append(monkey)

def operation(operator, second, value, prod):
    a = value
    if second == 'old':
        b = value
    else:
        b = int(second)

    if operator == "*":
        return a * b % prod
    else:
        return (a + b) % prod

def turn(monkey, prod):
    operator, second = monkey['operation']
    divisor = monkey['divisor']
    true_monkey = monkey['true']
    false_monkey = monkey['false']

    for item in monkey['items']:
        new_level = operation(operator, second, item, prod)
        if new_level % divisor == 0:
            monkeys[true_monkey]['items'].append(new_level)
        else:
            monkeys[false_monkey]['items'].append(new_level)
        monkey['inspections'] += 1
    monkey['items'] = []

prod = 1
for monkey in monkeys:
    prod *= monkey['divisor']

for i in range(10000):
    for monkey in monkeys:
        turn(monkey, prod)

a, b = 0, 0

for monkey in monkeys:
    if monkey['inspections'] > a:
        b = a
        a = monkey['inspections']
    elif monkey['inspections'] > b:
        b = monkey['inspections']

print(a * b)