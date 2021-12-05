raw = list(tuple(tuple(int(ol) for ol in ul.split(',')) for ul in el.strip().split(' -> ')) for el in open("input.txt").readlines())

N = 1000

table = list(list(0 for i in range(N)) for i in range(N))

for ((x1, y1), (x2, y2)) in raw:
    if x1 == x2 :
        for i in range(min(y1, y2), max(y1, y2) + 1):
            table[x1][i] += 1
    if y1 == y2 :
        for i in range(min(x1, x2), max(x1, x2) + 1):
            table[i][y1] += 1
    # this is for part 2
    if y1 != y2 and abs((x1 - x2) / (y1 - y2)) == 1:
        if x1 < x2 and y1 < y2 :
            for i in range(abs(x2 - x1) + 1):
                table[x1 + i][y1 + i] += 1
        elif x1 < x2 and y1 > y2 :
            for i in range(abs(x2 - x1) + 1):
                table[x1 + i][y1 - i] += 1
        elif x1 > x2 and y1 < y2 :
            for i in range(abs(x2 - x1) + 1):
                table[x1 - i][y1 + i] += 1
        elif x1 > x2 and y1 > y2 :
            for i in range(abs(x2 - x1) + 1):
                table[x1 - i][y1 - i] += 1

s = 0
for i in range(len(table)):
    for j in range(len(table)):
        if table[i][j] > 1:
            s += 1
print(s)