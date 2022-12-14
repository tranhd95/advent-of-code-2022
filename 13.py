from utils import puzzle_input
from functools import cmp_to_key

inp = puzzle_input("13")


def solve1(inp=inp):
    pairs = inp.split("\n\n")
    total = 0
    for i, pair in enumerate(pairs, start=1):
        fst, snd = tuple(map(eval, pair.split("\n")))
        if compare(fst, snd) < 0:
            total += i
    return total


def compare(l, r):
    match l, r:
        case int(), int():
            return l - r
        case int(), _:
            return compare([l], r)
        case _, int():
            return compare(l, [r])
        case list(), list():
            for l_, r_  in zip(l, r):
                if diff := compare(l_, r_):
                    return diff
            return len(l) - len(r)

def solve2(inp=inp):
    pairs = list(eval(line) for line in inp.split("\n") if line.strip())
    dividers = ([[2]], [[6]])
    pairs += dividers
    pairs.sort(key=cmp_to_key(compare))
    return (pairs.index(dividers[0]) + 1) * (pairs.index(dividers[1]) + 1)


print(solve1())
print(solve2())
