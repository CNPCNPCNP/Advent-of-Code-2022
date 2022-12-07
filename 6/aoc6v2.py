# 1 user command
# 2 other thing

class Dir():

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []

    def __hash__(self) -> int:
        (hash(self.name)) * (hash(self.parent))

    def __eq__(self, __o: object) -> bool:
        if isinstance(object, Dir):
            return self.name == object.name and self.parent == object.parent and self.children == object.children
        return False

with open(r'6\input.txt') as input:
    dirs = set()
    current = Dir("", "")
    for line in input:
        line = line.strip()
        line = line.split(" ")

        if line[0] == "$":
            if len(line) == 3:
                _, _, target = line
                if target == "..":
                    current = current.parent
                else:
                    dir = Dir(target, current)
                    if dir in dirs:
                        current = dir
                    else:
                        dirs.add(dir)
                    