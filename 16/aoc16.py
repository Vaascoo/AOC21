class BitVec:

    def __init__(self, string):
        self._vec = int(f'0b{string}', base=2)
        self._getter = 0b1 << len(string) - 1
        self._l = len(string)

    def __getitem__(self, index):
        if isinstance(index, slice):
            res = 0
            for i in range(*index.indices(self._l)):
                res = res << 1
                res += self.__getitem__(i)
            return res
        elif index < 0:
            index = self._l + index
        return int(bool(self._vec << index & self._getter))  # cursed

    def __str__(self) -> str:
        return f"{self._vec:b}"

    def __repr__(self) -> str:
        return self.__str__()


class Packet:
    def eval(self):
        pass


class Literal_Packet(Packet):

    def __init__(self, start, version, _type, value, _len):
        self._start = start
        self._version = version
        self._type = _type
        self._value = value
        self._len = _len

    def eval(self):
        return self._value


def prod(array):
    p = 1

    for el in array:
        p *= el

    return p


def greater(array):

    return array[0] > array[1]


def equal(array):
    return array[0] == array[1]


def less(array):
    return not greater(array) and not equal(array)


class Operations:

    OP_TABLE = {
        0: sum,
        1: prod,
        2: min,
        3: max,
        5: greater,
        6: less,
        7: equal,
    }

    @staticmethod
    def get(num):
        return Operations.OP_TABLE.get(num, lambda: 0)


class Operator_Packet(Packet):

    def __init__(self, start, version, _type, l_type):
        self._start = start
        self._version = version
        self._type = _type
        self._l_type = l_type
        self._op = Operations.get(self._type)
        self._value = bitvec[start + 7: start +
                             7 + (11 if self._l_type else 15)]
        self._len = (18 if self._l_type else 22)

    def eval(self, args):
        return self._op(self, args)


class Node:
    def __init__(self, head: Operator_Packet):
        self._head = head
        self._sub = None

    def eval(self):
        l = []
        if self._sub is None:
            return self._head._value

        for el in self._sub:
            l.append(el.eval())
        return self._head._op(l)


def convert(f):
    raw = list((int('0x' + el, base=16))
               for el in open(f"/home/vaascoo/Documents/Programming/rust/AOC21/16/{f}").read().strip())
    raw = list(f'{el:b}'.zfill(4) for el in raw)
    return "".join(raw)


raw = convert("input.txt")

bitvec = BitVec(raw)

nodes = dict()


def read_version(index):
    return bitvec[index: index + 3]


def read_type(index):
    return bitvec[index + 3: index + 6]


def read_length_id(index):
    return bitvec[index + 6]


def parse_literal(index):
    version, _type = read_version(index), read_type(index)
    acumulator = 0
    i = index + 6

    while 0b10000 & bitvec[i: i + 5]:
        acumulator <<= 4
        acumulator += bitvec[i + 1: i + 5]
        i += 5

    acumulator <<= 4
    acumulator += bitvec[i + 1: i + 5]

    return (i + 5) - index, [Literal_Packet(index, version, _type, acumulator, (i + 5) - index)]


def parse_operator(index):

    l_id = read_length_id(index)

    return (18 if l_id else 22), [Operator_Packet(index, read_version(index), read_type(index), l_id)]


def auto_parse(index):
    return parse_literal(index) if read_type(index) == 4\
        else parse_operator(index)


def parse(index):

    pckts = []

    while index < bitvec._l - 7:
        inc, packet = auto_parse(index)
        pckts += packet
        index += inc

    return pckts


def p1(l):
    s = 0
    for el in l:
        s += el._version
    return s


def build_sub_tree(index, packets):

    head = packets[index]

    node = Node(head)

    nodes[index] = node

    if isinstance(node._head, Literal_Packet):
        return index, node._head._len

    elif isinstance(node._head, Operator_Packet):
        l, i = 0, index + 1
        node._sub = []
        if node._head._l_type == 0:

            while l < node._head._value and i < len(packets):
                old_i = i
                i, new_len = build_sub_tree(i, packets)
                node._sub.append(nodes[old_i])
                l += new_len
                i += 1
            return i - 1, node._head._len + node._head._value
        else:
            while len(node._sub) < node._head._value:
                old_i = i
                i, new_len = build_sub_tree(i, packets)
                node._sub.append(nodes[old_i])
                i += 1
                l += new_len
            return i - 1, l + node._head._len


packets = parse(0)

print(p1(packets))

build_sub_tree(0, packets)

print(nodes[0].eval())
