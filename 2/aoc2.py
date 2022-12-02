values = {"X": 1, "Y": 2, "Z": 3}

wins = {"X": 0, "Y": 3, "Z": 6}

beats = {("A", "X"): 3, ("A", "Y"): 6, ("A", "Z"): 0,
         ("B", "X"): 0, ("B", "Y"): 3, ("B", "Z"): 6,
         ("C", "X"): 6, ("C", "Y"): 0, ("C", "Z"): 3}

# A, X ROCK
# B, Y PAPER
# C, Z SCISSORS

conversions = {("A", "X"): "Z", ("A", "Y"): "X", ("A", "Z"): "Y",
               ("B", "X"): "X", ("B", "Y"): "Y", ("B", "Z"): "Z",
               ("C", "X"): "Y", ("C", "Y"): "Z", ("C", "Z"): "X"}

points = 0

with open("input.txt") as input:
    for line in input:
        line = line.strip()
        elf, player = line.split(" ")
        print(elf, player)
        points += wins[player]
        points += values[conversions[(elf, player)]]

print(points)
