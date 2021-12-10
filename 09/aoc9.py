import copy

# good spaghetti

raw = list(list(map(lambda x : int(x), list(el.strip()))) for el in open("/home/vaascoo/Documents/Programming/rust/AOC21/9/input.txt"))

def print_matrix():
    global raw
    for line in raw:
        print(line)
    print(".")


def bfs(i, j):
    global raw
    global visited
    res = 0
    queue = [(i, j)]
    visited[i][j] = True
    while queue != []:
        pos = queue.pop(0)
        res += 1
        for el in ((pos[0] - 1, pos[1]), (pos[0] + 1, pos[1]), (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)):
            try:
                assert el[0] >= 0 and el[1] >= 0 and el[0] < len(raw) and el[1] < len(raw[0])
                assert raw[el[0]][el[1]] != 9
                #print(raw[el[0]][el[1]])
                if raw[el[0]][el[1]] > raw[pos[0]][pos[1]] and not visited[el[0]][el[1]]:
                    queue.append(el)
                    visited[el[0]][el[1]] = True
            except:
                pass
        #print_matrix()
    return res

visited = copy.deepcopy(raw)
for i in range(len(raw)):
    for j in range(len(raw[0])):
        visited[i][j] = False

s = 0

d = dict()

for i in range(len(raw)):
    for j in range(len(raw[0])):
        f = True
        for el in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            try:
                assert el[0] >= 0 and el[1] >= 0 and el[0] < len(raw) and el[1] < len(raw[0])
                if raw[i][j] >= raw[el[0]][el[1]]:
                    f = False
            except:
                pass
        if f:
            d[(i, j)] = raw[i][j]
            s += 1 + raw[i][j]

#print(raw)
print(s)
sizes = []

for el in d:
    sizes.append(bfs(*el))

sizes.sort(reverse=True)

print(sizes[0] * sizes[1] * sizes[2])