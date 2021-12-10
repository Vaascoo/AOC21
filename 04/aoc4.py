from collections import OrderedDict

def check_line(index, board, map):
    i = 0
    for j in range(len(board)):
        i = max(i, map.get(board[index][j]))
    return i

def check_col(index, board, map):
    i = 0
    for j in range(len(board)):
        i = max(i, map.get(board[j][index]))
    return i

def compute_board(board, draw_map):
    indexes = []
    for i in range(len(board)):
        indexes.append(check_line(i, board, draw_map))

    for i in range(len(board)):
        indexes.append(check_col(i, board, draw_map))
    
    return (min(indexes), bool(len(indexes) // 5), len(indexes) % 5)

def compute_score(b_index, tup):
    global boards
    global draw_set
    global draw
    last_index, isCol, index = tup
    board = boards[b_index]
    s = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if draw_set.get(board[i][j]) <= last_index:
                pass
            else:
                s += board[i][j]
    return s * draw[last_index]
        


    
with open("/home/vaascoo/Documents/Programming/rust/AOC21/4/input.txt", "r") as f:
    draw = list(int(el) for el in f.readline().strip().split(','))
    f.readline()
    raw = list(map(lambda s : list(int(el) for el in s.replace('  ', ' ').strip().split(' ')), list(filter(lambda s : s != '\n', f.readlines()))))

boards = []
for i in range(5, len(raw) + 5, 5):
    boards.append(raw[i - 5 : i])
draw_set = OrderedDict()
for i in range(len(draw)):
    draw_set[draw[i]] = i

winner = float('inf')
winner_index = None
winner_tuple = None

last = -1
last_index = None
last_tuple = None

i = 0
for board in boards:
    tup = compute_board(board, draw_set)
    if (tup[0] < winner):
        winner = tup[0]
        winner_index = i
        winner_tuple = tup
    if (tup[0] > last):
        last = tup[0]
        last_index = i
        last_tuple = tup
    i += 1

print(compute_score(winner_index, winner_tuple))
print(compute_score(last_index, last_tuple))