raw = list(map(lambda s : list(int(el) for el in tuple(s)), list(line.strip() for line in open("/home/vaascoo/Documents/Programming/rust/AOC21/11/input.txt").readlines())))

flash_counter, to_flash, flashed, STEPS = 0, None, None, 10000

def get_adj(i, j):
    global raw
    for ii, jj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i - 1, j - 1), (i - 1, j + 1), (i + 1, j + 1), (i + 1, j - 1)):
        if ii >= 0 and jj >= 0 and ii < len(raw) and jj < len(raw[0]):
            yield (ii, jj)

def flash(i, j):
    global raw, to_flash, flash_counter, flashed
    flash_counter += 1
    flashed.add((i, j))
    for x, y in get_adj(i, j):
        if (x, y) not in to_flash and (x, y) not in flashed:
            raw[x][y] = (raw[x][y] + 1) % 10
            
            if raw[x][y] == 0:
                flash(x, y)

for _ in range(STEPS):
    to_flash = set()
    flashed = set()

    
    for i in range(len(raw)):
        for j in range(len(raw[0])):
            raw[i][j] = (raw[i][j] + 1) % 10
            if raw[i][j] == 0:
                to_flash.add((i, j))

    for el in to_flash:
        flash(*el)
    
    # part2
    if len(flashed) == 100:
        print(_ + 1)
        break

#steps = 100 for part1
print(flash_counter)
