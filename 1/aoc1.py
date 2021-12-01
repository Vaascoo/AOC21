raw = list(int(el.strip()) for el in open("input.txt").readlines())

count1, count2 = 0, 0
for i in range(1, len(raw) - 2):
    if sum(raw[i: i + 3]) > sum(raw[i - 1: i + 2]):
        count2 += 1
    if(raw[i] > raw[i - 1]):
        count1 += 1

for i in range(len(raw) - 2, len(raw)):
    if(raw[i] > raw[i - 1]):
        count1 += 1

print(count1)
print(count2)
