import re

paths = {}

def compute_max_y(vx, vy, range_x, range_y):
    x, y = 0, 0
    max_y = -1
    passed = False
    xx, yy = vx, vy
    
    while vx != 0 or y >= range_y.stop :

        
        x, y = x + vx, y + vy
        paths.update({(xx, yy) : paths.get((xx, yy), []) + [(x, y)]})
        max_y = max(max_y, y)
        vx -= 1 if vx > 0 else 0
        vy -= 1

        if range_x.start <= x < range_x.stop and range_y.start <= y < range_y.stop:
            passed = True

    return passed, max_y
        

raw = open("/home/vaascoo/Documents/Programming/rust/AOC21/17/input.txt").read()

target = [list(int(ul) for ul in el.split('..')) for el in re.findall(r"-?[0-9]+\.\.-?[0-9]+", raw)]

for i, el in enumerate(target):
    el[1] += 1
    target[i] = range(*el)

print(f"{target}")

maxy = -1
last = None
_pass = set()

for vx in range(0,500):
    print(vx)
    for vy in range(-100, 200):
        passed, y = compute_max_y(vx, vy, target[0], target[1])
        if passed and y > maxy:
            maxy = y
            last = (vx, vy)
        if passed:
            _pass.add((vx, vy))

print(last)
print(maxy)
print(len(_pass))