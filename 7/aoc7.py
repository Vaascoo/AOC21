raw = list(int(el) for el in open("/home/vaascoo/Documents/Programming/rust/AOC21/7/input.txt").readline().split(','))

a = []
for n in range(max(raw)): #posicao
    v = list(abs(pos - n) * (abs(pos - n) + 1) // 2 for pos in raw)
    a.append(sum(v))

print(min(a))
