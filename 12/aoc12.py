raw = list(tuple(ul.strip() for ul in el.split('-')) for el in open("/home/vaascoo/Documents/Programming/rust/AOC21/12/input.txt"))

graph = {}

for u, v in raw:

    if u not in graph:
        graph[u] = [v]
    else:
        graph[u].append(v)

    if v not in graph:
        graph[v] = [u]
    else:
        graph[v].append(u)

def p1(start, end, visited = set()):
    res = 0
    new_visited = visited.union({start})

    if start == end:
        return 1

    for cave in graph[start]:
        if cave not in visited or cave.isupper():
                res += p1(cave, end, new_visited)
    return res

def p2(start, end, visited = set(), repeated = None):
    res = 0
    _visited = visited.union({start})

    if start == end:
        return 1

    for v in graph[start]:
        if v not in visited or v.isupper():
            res += p2(v, end, _visited, repeated)
        elif v in visited and repeated is None and v not in ("start", "end"):
            res += p2(v, end, _visited, v)
    return res


print(p1("start", "end"))
print(p2("start", "end"))