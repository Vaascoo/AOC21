raw = list(el.strip() for el in open("/home/vaascoo/Documents/Programming/rust/AOC21/10/input.txt").readlines())

# () - 3
# [] - 57
# {} - 1197
# >> - 25137

openings = set(('(', '[', '{', '<'))
closings = set((')', ']', '}', '>'))
score = 0

for i in range(len(raw) - 1, -1, -1):
    line = raw[i]
    stack = []
    for char in line:
        if char in openings:
            stack.append(char)
        elif char in closings:
            if char == ')':
                if stack[-1] == '(':
                    stack.pop(-1)
                else:
                    score += 3
                    del(raw[i])
                    break
            elif char == ']':
                if stack[-1] == '[':
                    stack.pop(-1)
                else:
                    score += 57
                    del(raw[i])
                    break
            elif char == '}':
                if stack[-1] == '{':
                    stack.pop(-1)
                else:
                    score += 1197
                    del(raw[i])
                    break
            elif char == '>':
                if stack[-1] == '<':
                    stack.pop(-1)
                else:
                    score += 25137
                    del(raw[i])
                    break

print(score)

# *= 5 + 
# () - 1
# [] - 2
# {} - 3
# <> - 4

def get_score(char):
    scores = {
        '(' : 1,
        '[' : 2,
        '{' : 3,
        '<' : 4
    }
    return scores.get(char)



scores = []
for line in raw:
    score = 0
    stack = []
    for char in line:
        c = None
        if char in openings:
            stack.append(char)
        elif char in closings:
            if char == ')':
                if stack[-1] == '(':
                    stack.pop(-1)
            elif char == ']':
                if stack[-1] == '[':
                    stack.pop(-1)
            elif char == '}':
                if stack[-1] == '{':
                    stack.pop(-1)
            elif char == '>':
                if stack[-1] == '<':
                    stack.pop(-1)
    
    while len(stack) and (char := stack.pop(-1)):
        score *= 5
        score += get_score(char)
                

    scores.append(score)

scores.sort()
print(scores[len(scores) // 2])