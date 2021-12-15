import heapq

raw = list(list(int(ul) for ul in el.strip()) for el in open("/home/vaascoo/Documents/Programming/rust/AOC21/15/input.txt").readlines())

large = list(list(0 for __ in range(len(raw[0] * 5))) for _ in range(len(raw) * 5))

for k in range(5):
    for i in range(len(raw)):
        for j in range(len(raw[0])):
            if k == 0:
                large[i + k * len(raw)][j] = raw[i][j]
            else:
                x  = large[i + (k - 1) * len(raw)][j] + 1
                if x > 9:
                    x -= 9
                large[i + k * len(raw)][j] = x

for line in large:
    for i in range(len(raw[0])):
        for k in range(5):
            if (new := line[i] + k) > 9:
                new -= 9
            line[i + k * len(raw)] = new

                


def get_nbr(i, j):
    for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
        if x >= 0 and y >= 0 and x < len(raw) and y < len(raw[0]):
            yield (x, y)

def djikstra():

    queue = []

    path = dict()

    heapq.heappush(queue, (0, (0, 0)))

    dists = dict()
    dists[(0, 0)] = 0

    while len(queue) != 0:
        _, pos = heapq.heappop(queue)

        for x, y in get_nbr(*pos):
            if dists.get((x, y), float('inf')) > dists[pos] + raw[x][y]:
                dists[(x, y)] = dists[pos] + raw[x][y]
                path[(x, y)] = pos
                heapq.heappush(queue, (dists[pos] + raw[x][y], (x, y)))
                if (x, y) == (len(raw) - 1, len(raw[0]) - 1):
                    break

    return dists[(len(raw) - 1, len(raw[0]) - 1)]



print(djikstra())

raw = large

print(djikstra())