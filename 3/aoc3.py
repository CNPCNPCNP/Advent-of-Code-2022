from collections import Counter

with open("3\input.txt") as input:
    priority = 0

    for line in input:
        line = line.strip()
        length = len(line)

        compartment_1 = line[:length // 2]
        compartment_2 = line[length // 2:]
        
        seen = set()
        for letter in compartment_1:
            if letter in compartment_2 and letter not in seen:
                if letter.isupper():
                    priority += ord(letter) - ord("A") + 27
                else:
                    priority += ord(letter) - ord('a') + 1
                seen.add(letter)
        
with open("3\input.txt") as input:
    priority2 = 0
    counter = 0
    combined = []

    for line in input:
        line = line.strip()
        length = len(line)

        if counter < 3:
            combined.append(set(line))
            counter += 1
        if counter == 3:
            print(combined)
            a, b, c = combined
            common, = a.intersection(b).intersection(c)
            print(common)

            if common.isupper():
                priority2 += ord(common) - ord("A") + 27
            else:
                priority2 += ord(common) - ord('a') + 1

            counter = 0
            combined = []

print(priority2)