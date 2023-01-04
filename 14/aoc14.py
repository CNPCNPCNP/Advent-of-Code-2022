sensors = []
beacons = []
distances = []

with open(r'14\input.txt') as input:
    for index, line in enumerate(input):
        line = line.strip()
        line = line.split(" ")

        sensor_x = int(line[2][2:-1])
        sensor_y = int(line[3][2:-1])
        sensors.append((sensor_x, sensor_y))

        beacon_x = int(line[-2][2:-1])
        beacon_y = int(line[-1][2:])
        beacons.append((beacon_x, beacon_y))

        distances.append(abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y))

print(sensors)
print(beacons)
print(distances)

y_target = 2000000
overlaps = set()
for sensor, distance in zip(sensors, distances):
    x, y = sensor
    if distance < abs(y_target - y):
        continue
    if y <= y_target:
        distance -= y_target - y
        overlaps.add((x, y_target))
        xl = x
        xr = x
        while distance > 0:
            left = xl - 1, y_target
            right = xr + 1, y_target
            xl -= 1
            xr += 1
            overlaps.add(left)
            overlaps.add(right)
            distance -= 1
    else:
        distance -= y - y_target
        overlaps.add((x, y_target))
        xl = x
        xr = x
        while distance > 0:
            left = xl - 1, y_target
            right = xr + 1, y_target
            xl -= 1
            xr += 1
            overlaps.add(left)
            overlaps.add(right)
            distance -= 1

overlaps = overlaps.difference(set(beacons))
print(len(overlaps))

possibles = set()

for sensor, distance in zip(sensors, distances):
    print(sensors.index(sensor))
    x, y = sensor
    sbd = distance + 1
    nx = x
    ny = y - sbd
    while ny > y:
        if ny >= 0 and nx <= 4000000 and nx >= 0 and ny <= 4000000:
            possibles.add((nx, ny))
        nx += 1
        ny -= 1
    while nx > x:
        if ny >= 0 and nx <= 4000000 and nx >= 0 and ny <= 4000000:
            possibles.add((nx, ny))
        nx -= 1
        ny -= 1
    while ny < y:
        if ny >= 0 and nx <= 4000000 and nx >= 0 and ny <= 4000000:
            possibles.add((nx, ny))
        nx -= 1
        ny += 1
    while nx < x:
        if ny >= 0 and nx <= 4000000 and nx >= 0 and ny <= 4000000:
            possibles.add((nx, ny))
        nx += 1
        ny += 1
    
def possible_location(start, sensor, distance):
    sx, sy = start
    fx, fy = sensor
    return abs(fx - sx) + abs(fy - sy) > distance

print(len(possibles))

for possible in possibles:
    for sensor, distance in zip(sensors, distances):
        test = possible_location(possible, sensor, distance)
        if not test:
            break
    if test:
        print(possible)
