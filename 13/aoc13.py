import re

class Orientation:
    HORIZONTAL = 0
    VERTICAL = 1

points = []
rules = []

def print_grid():
    x, _ = max(points, key=lambda n : n[0])
    _, y = max(points, key=lambda n : n[1])
    grid = list(list("." for _ in range(x + 1)) for __ in range(y + 1))
    for i, j in points:
        grid[j][i] = "■"
    
    for line in grid:
        print("".join(line))

    print("--")



for line in open("/home/vaascoo/Documents/Programming/rust/AOC21/13/input.txt").readlines():
    line = line.strip()
    if re.match(r"[0-9]+,[0-9]+", line):
        points.append(list(int(el) for el in line.split(',')))
    elif re.match(r"fold along (x|y)=[0-9]+", line):
        number = re.search(r"[0-9]+", line).group()
        if 'x' in line:
            rules.append([Orientation.HORIZONTAL, int(number)])
        else:
            rules.append([Orientation.VERTICAL, int(number)])

for rule in rules:
    orientation = rule[0]
    for i in range(len(points) - 1, -1 , -1):
        if points[i][orientation] > rule[1]:
            points[i][orientation] = 2 * rule[1] - points[i][orientation]
        if points[i][orientation] == rule[1]:
            del points[i][orientation]
    # s = set((el[0], el[1]) for el in points) \
    # print(len(s))                            - Part 1
    # break                                    /
    print_grid()
