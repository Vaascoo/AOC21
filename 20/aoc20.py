ITERATIONS = 50#2

with open("/home/vaascoo/Documents/Programming/AOC21/20/input.txt", "r") as f:
    enhancement = list(int(el == '#') for el in f.readline().strip())

    f.readline()

    previous = set()
    for i, line in enumerate(f.readlines()):
        for j, el in enumerate(line.strip()):
            if el == '#':
                previous.add((i, j))

counter = None

for iter in range(ITERATIONS):

    current = set()

    mini, maxi = min(previous, key=lambda x : x[0])[0], max(previous, key=lambda x : x[0])[0]
    minj, maxj = min(previous, key=lambda x : x[1])[1], max(previous, key=lambda x : x[1])[1]

    for i in range(mini - 1, maxi + 2):
        for j in range(minj - 1, maxj + 2):
            acc = 0
            for ii in range(i - 1, i + 2):
                for jj in range(j - 1, j + 2):
                    acc = acc << 1
                    if (ii, jj) in previous:
                        acc += 1
                    elif  mini <= ii <= maxi and minj <= jj <= maxj:
                        pass
                    else:
                        if iter % 2:
                            acc += 1

            if enhancement[acc]:
                current.add((i, j))

    previous = current


print(len(current))
