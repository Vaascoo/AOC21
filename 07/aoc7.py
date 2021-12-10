raw = list(int(el) for el in open("input.txt").readline().split(','))

a = []
for n in range(max(raw)): #posicao
    v = list(abs(pos - n) * (abs(pos - n) + 1) // 2 for pos in raw)
    a.append(sum(v))

print(min(a))
