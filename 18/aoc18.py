def parse_number(string, index, limit):
    number = 0
    o_index = index
    while index < limit and 48 <= (char := ord(string[index])) <= 57:
        number = number * 10 + char % 48
        index += 1
    return index - o_index, number

# pair := [int | pair, int | pair]
def parse_list(string, index, limit):
    stack = [1]
    res = []
    o_index = index

    assert string[index] == '[' and string[limit - 1] == ']'

    index += 1

    while index < limit:
        
        if 48 <= ord(string[index]) <= 57:
            n, x = parse_number(string, index, limit)
            index += n
            res.append(x)
        
        elif string[index] == ',':
            index += 1
        
        elif string[index] == '[':
            n, l = parse_list(string, index, limit)
            stack.append(1)
            res.append(l)
            index += n
    
        elif string[index] == ']':
            stack.pop(-1)
            if not len(stack):
                return index - o_index, res
            index += 1

def parse(string):
    return parse_list(string, 0, len(string))

def flatten(lst, depth = 1):
    l = []
    
    for el in lst:
        if isinstance(el, list):
            l += flatten(el, depth + 1)
        else:
            l.append((el, depth))
    
    return l

def explode(lst : list):
    exploded = False
    for i, pair in enumerate(lst):
        n, depth = pair
        if depth > 4:
            exploded = True
            if i > 0:
                lst[i - 1] = (lst[i - 1][0] + lst[i][0], lst[i - 1][1])
            if i < len(lst) - 2:
                lst[i + 2] = (lst[i + 2][0] + lst[i + 1][0], lst[i + 2][1])
            break
    if exploded:
        depth = lst.pop(i + 1)[1]
        lst.pop(i)
        lst.insert(i, (0, depth - 1))
    return exploded

def split(lst : list):
    _split = False
    for i, pair in enumerate(lst):
        n, depth = pair
        if n > 9:
            _split = True
            break
    if _split:
        l, r = (n // 2, depth + 1), (int(n / 2 + 0.5), depth + 1)
        lst.pop(i)
        lst.insert(i, r)
        lst.insert(i, l)
    
    return _split

def reduce(lst):
    while(explode(lst) or split(lst)):
        pass

def get_deepest(lst):
    return max(lst, key = lambda p : p[1])[1]

def magnitude(lst : list, level):
    index = 0
    while index < len(lst) - 1:
        if lst[index][1] == level:
            if lst[index + 1][1] == level:
                magn = 3 * lst[index][0] + 2 * lst[index + 1][0]
                n_pair = (magn, level - 1)
                lst.pop(index + 1)
                lst.pop(index)
                lst.insert(index, n_pair)
                index += 1
                continue
        index += 1

def list_magnitude(lst):
    top_level = get_deepest(lst)
    while top_level > 0:
        magnitude(lst, top_level)
        top_level -= 1


raw = list(el.strip() for el in open("/home/vaascoo/Documents/Programming/rust/AOC21/18/input.txt").readlines())

numbers = []

for i, el in enumerate(raw):
    _, raw[i] = parse(el)
    raw[i] = flatten(raw[i])

acumulated = raw[0]

for i in range(1, len(raw)):
    new = acumulated + raw[i]
    for j in range(len(new)):
        new[j] = (new[j][0], new[j][1] + 1)
    reduce(new)
    acumulated = new

# print(acumulated)

list_magnitude(acumulated)

print(acumulated)

m = -1

for i in range(len(raw)):
    for j in range(i + 1, len(raw)):
        new = raw[i] + raw[j]
        for z in range(len(new)):
            new[z] = (new[z][0], new[z][1] + 1)
        reduce(new)
        list_magnitude(new)
        m = max(m, new[0][0])

        # spaghetti
        new = raw[j] + raw[i]
        for z in range(len(new)):
            new[z] = (new[z][0], new[z][1] + 1)
        reduce(new)
        list_magnitude(new)
        m = max(m, new[0][0])

print(m)