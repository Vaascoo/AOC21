raw = list(int(el) for el in open("input.txt").readline().split(','))

COUNTER = 256

days = list(0 for i in range(9))

for el in raw:
        days[el] += 1

for _ in range(COUNTER):
    day0 = days[0]
    for i in range(1, len(days)):
        days[i - 1] = days[i] 
    days[8] = day0
    days[6] += day0

print(sum(days))
