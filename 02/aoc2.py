import re

raw = list(el.strip() for el in open("input.txt").readlines())

pos = [0, 0]
aim = 0

for el in raw:
    if "forward" in el:
        num = int(el.split(' ')[1])
        pos[1] += aim * num
        pos[0] += num
    elif "down" in el:
        num = int(el.split(' ')[1])
        #pos[1] += num
        aim += num
    elif "up" in el:
        num = int(el.split(' ')[1])
        #pos[1] -= num
        aim -= num

print(f"{pos[0] * pos[1]}")
print(f"{aim}")
