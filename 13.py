from utils import puzzle_input
from functools import cmp_to_key

inp = puzzle_input("13")


def solve1(inp=inp):
    pairs = inp.split("\n\n")
    total = 0
    for i, pair in enumerate(pairs, start=1):
        fst, snd = tuple(map(eval, pair.split("\n")))
        if compare(fst, snd) == -1: 
            total += i
    return total


def compare(a, b):
    match (a, b):
        case (int(), int()):
            if a == b:
                return 0
            return -1 if a < b else 1
        case (int(), _):
            a = [a]
        case (_, int()):
            b = [b]

    for i in range(len(a)):
        if i >= len(b):
            return 1
        if cmp := compare(a[i], b[i]):
            return cmp

    return 0 if len(a) == len(b) else -1

def solve2(inp=inp):
    pairs = list(eval(line) for line in inp.split("\n") if line.strip())
    dividers = ([[2]], [[6]])
    pairs += dividers
    pairs.sort(key=cmp_to_key(compare))
    return (pairs.index(dividers[0]) + 1) * (pairs.index(dividers[1]) + 1)


print(solve1())
print(solve2())
