with open("4\input.txt") as input:
    count = 0
    count2 = 0
    for line in input:
        line = line.strip()
        first, second = line.split(",")
        f1, f2 = first.split("-")
        f3, f4 = second.split("-")
        if int(f1) >= int(f3) and int(f2) <= int(f4) or int(f3) >= int(f1) and int(f4) <= int(f2):
            count += 1

        f1 = int(f1)
        f2 = int(f2)
        f3 = int(f3)
        f4 = int(f4)

        r1 = set(range(f1, f2 + 1))
        r2 = set(range(f3, f4 + 1))
        
        if r1.intersection(r2):
            count2 += 1


print(count, count2)