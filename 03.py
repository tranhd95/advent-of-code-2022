import string

from utils import puzzle_input

priorities = list(string.ascii_lowercase + string.ascii_uppercase)

def solve1(inp):
    score = 0
    for line in inp.split("\n"):
        mid = len(line)//2
        fst, snd = line[:mid], line[mid:]
        shared = set(fst) & set(snd)
        score += sum(priorities.index(s) + 1 for s in shared)
    print(score)

def solve2(inp):
    score = 0
    it = iter(inp.split("\n"))
    for a, b, c in zip(it, it, it):
        shared = set(a) & set(b) & set(c)
        score += sum(priorities.index(s) + 1 for s in shared)
    print(score)


solve1(puzzle_input("3"))
solve2(puzzle_input("3"))
