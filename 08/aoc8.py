#spaghetti af


raw = list(el.strip() for el in open("/home/vaascoo/Documents/Programming/rust/AOC21/8/input.txt").readlines())

chars = {
    0: set(('a', 'b', 'c', 'e', 'f', 'g')),
    1: set(('c', 'f')),
    2: set(('a', 'c', 'd', 'e', 'g')),
    3: set(('a', 'c', 'd', 'f', 'g')),
    4: set(('b', 'c', 'd', 'f')),
    5: set(('a', 'b', 'd', 'f', 'g')),
    6: set(('a', 'b', 'd', 'e', 'f', 'g')),
    7: set(('a', 'c', 'f')),
    8: set(('a', 'b', 'c', 'd', 'e', 'f', 'g')),
    9: set(('a', 'b', 'c', 'd', 'f', 'g')),
}

lengths = {6: [0, 6, 9], 2: [1], 5: [2, 3, 5], 4: [4], 3: [7], 7: [8]}

i = 0

commons = {
    0 : set(()),
    2 : None,
    3 : None,
    5 : None,
    6 : None,
    9 : None
}

# 1, 4, 7, 8 just length
# 0, 2, 3, 5, 6, 9

soma = 0

for line in raw:
    a, b = line.split(' | ')
    a = a.split(' ')
    b = b.split(' ')

    d = {1 : set(), 4 : set(), 7 : set(), 8 : set(), 0 : set(), 2 : set(), 3 : set(), 5 : set(), 6 : set(), 9 : set()}
    
    for i in range(len(a)):
        if len(lengths.get(len(a[i]))) == 1:
            d[lengths.get(len(a[i]))[0]] = set(a[i])
    
    for i in range(len(a)):
        if len(lengths.get(len(a[i]))) != 1:
            s = set(a[i])
            for el in lengths.get(len(a[i])):
                if len(s) == 6:
                    if d[4].issubset(s):
                        d[9] = s
                    elif d[7].issubset(s):
                        d[0] = s
                    else:
                        d[6] = s
                else:
                    if s.issuperset(d[7]):
                        d[3] = s
                    if s.issubset(d[6]):
                        d[5] = s
                    
    
    for i in range(len(a)):
        if len(lengths.get(len(a[i]))) != 1:
            s = set(a[i])
            for el in lengths.get(len(a[i])):
                if len(s) == 6:
                    if d[4].issubset(s):
                        d[9] = s
                    elif d[7].issubset(s):
                        d[0] = s
                    else:
                        d[6] = s
                else:
                    if s.issuperset(d[7]):
                        d[3] = s
                    if s.issubset(d[6]):
                        d[5] = s
                    

    number = []
    for el in b:
        s = set(el)
        flag = True
        for no in d:
            if s.issubset(d[no]) and d[no].issubset(s):
                number.append(str(no))
                flag = False
                break
        if flag:
            number.append('2')

    soma += int("".join(number))
    number = []


print(soma)
    
