import copy
raw = list(el.strip() for el in open("input.txt").readlines())
copy1, copy2 = [], []
count = [0 for i in range(len(raw[0]))]
total = len(raw)


for el in raw:
    for i in range(len(el)):
        if el[i] == '0':
            pass
        else:
            count[i] += 1

gamma, epsilon = 0, 0

n = 0
for el in count[::-1]:
    if el >= len(raw) // 2:
        gamma += 2 ** n
    else:
        epsilon += 2 ** n
    n += 1

print(f"{gamma * epsilon}")


for el in raw:
    copy1.append(el)
    copy2.append(el)

for i in range(len(count)): count[i] = 0

outer = len(raw[0])

for i in range(outer):
    if len(copy1) == 1:
        break
    for j in range(len(copy1)):
        if copy1[j][i] == '1':
            count[i] += 1
    
    if count[i] >= len(copy1) - count[i]:
        copy1 = list(filter(lambda s : s[i] == '1', copy1))
    else:
        copy1 = list(filter(lambda s : s[i] != '1', copy1))

for i in range(len(count)): count[i] = 0

for i in range(outer):
    if len(copy2) == 1:
        break
    for j in range(len(copy2)):
        if copy2[j][i] == '1':
            count[i] += 1
    
    if count[i] >= len(copy2) - count[i]:
        copy2 = list(filter(lambda s : s[i] == '0', copy2))
    else:
        copy2 = list(filter(lambda s : s[i] == '1', copy2))


o2 = int(f'0b{copy1[0]}', base=2)
co2 = int(f'0b{copy2[0]}', base=2)

print(f"{o2 * co2}")