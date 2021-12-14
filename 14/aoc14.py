from collections import OrderedDict

with open("/home/vaascoo/Documents/Programming/rust/AOC21/14/input.txt", "r") as f:
    template = f.readline().strip()
    f.readline()
    rules = dict(tuple(el.strip().split(' -> ')) for el in f.readlines())


STEPS = 40
sequences = OrderedDict()
count = dict()

for i in range(len(template) - 1):
    sequences.update({template[i:i + 2] : sequences.get(template[i:i + 2], 0) + 1})

for letter in template:
    if letter in count:
        count[letter] += 1
    else:
        count[letter] = 1


for _ in range(STEPS):
    new_dict = OrderedDict()
    for pair in sequences:
        if pair in rules:
            new = rules[pair]
            p1, p2 = pair[0] + new, new + pair[1]
            new_letters = sequences[pair]
            new_dict.update({ p1: new_dict.get(p1, 0) + sequences[pair]})
            new_dict.update({ p2: new_dict.get(p2, 0) + sequences[pair]})
            count.update({new: count.get(new, 0) + new_letters})
        else:
            new_dict.update({pair: sequences[pair]})
    
    sequences = new_dict

    del new_dict
#print(sequences)
#print(count)

print(count[max(count, key=count.__getitem__)] - count[min(count, key=count.__getitem__)])