from utils import puzzle_input
from collections import defaultdict


def neighbourhood(x, y):
    yield (x, y + 1)
    yield (x + 1, y)
    yield (x, y - 1)
    yield (x - 1, y)


def parse_input(inp):
    hmap = defaultdict(lambda: None)
    src, dest = None, None
    for y, row in enumerate(inp.split("\n")):
        for x, h in enumerate(row):
            n = (x, y)
            hmap[n] = h
            if h == "S":
                src = n
                hmap[n] = "a"
            if h == "E":
                hmap[n] = "z"
                dest = n
    return hmap, src, dest

def bfs(hmap, src, arrived, is_legal_move):
    Q = [src]
    seen = {src}
    dist = defaultdict(lambda: 0)
    while Q:
        v = Q.pop(0)
        vh = hmap[v]
        if arrived(v):
            return dist[v]
        for n in neighbourhood(*v):
            nh = hmap[n]
            if n not in seen and nh is not None and is_legal_move(vh, nh):
                seen.add(n)
                Q.append(n)
                dist[n] += dist[v] + 1

def solve1(hmap, src, dest):
    arrived = lambda n: n == dest
    is_legal_move = lambda frm, to: ord(to) - ord(frm) <= 1
    return bfs(hmap, src, arrived, is_legal_move)

def solve2(hmap, src, dest):
    arrived = lambda n: hmap[n] == 'a'
    is_legal_move = lambda frm, to: ord(frm) - ord(to) <= 1
    return bfs(hmap, dest, arrived, is_legal_move)


parsed_input = parse_input(puzzle_input("12"))

print(solve1(*parsed_input))
print(solve2(*parsed_input))
