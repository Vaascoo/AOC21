raw = list(el.strip() for el in open("/home/vaascoo/Documents/Programming/rust/AOC21/10/input.txt").readlines())

score1, scores, score2 = 0, [], 0
correspondence, points = dict(zip(('(', '[', '{', '<'), (')', ']', '}', '>'))), dict(zip((')', ']', '}', '>'), (3, 57, 1197, 25137)))
points2 = dict(zip(('(', '[', '{', '<'), (1, 2, 3, 4)))

for line in raw:
    stack, corrupt, score2 =  [], False, 0
    for char in line:
        if char in correspondence:
            stack.append(char)
        else:
            if char == correspondence.get(stack[-1]):
                stack.pop(-1)
            else: #part1
                score1 += points.get(char)
                corrupt = True
                break
    #part2
    while not corrupt and len(stack) and (char := stack.pop(-1)):
        score2 *= 5
        score2 += points2.get(char)
    if not corrupt:
        scores.append(score2)

print(score1)
print(sorted(scores)[len(scores) // 2])
