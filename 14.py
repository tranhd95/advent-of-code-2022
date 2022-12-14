from collections import defaultdict
from utils import puzzle_input


def gen_cave(inp):
    cave = defaultdict(lambda: ".")
    cave[(500, 0)] = "+"
    for line in inp.split("\n"):
        points = [tuple(map(int, point.split(","))) for point in line.split(" -> ")]
        for (x1, y1), (x2, y2) in zip(points, points[1:]):
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2)+1):
                    cave[(x1, y)] = "#"
            else:
                for x in range(min(x1, x2), max(x1, x2)+1):
                    cave[(x, y1)] = "#"
    return cave

def print_cave(cave):
    min_x, min_y = min(x for x, _ in cave.keys()), min(y for _, y in cave.keys())
    max_x, max_y = max(x for x, _ in cave.keys()), max(y for _, y in cave.keys())
    for y in range(min_y, max_y+1):
        print(f"{y} ", end=" ")
        for x in range(min_x, max_x+1):
            print(cave[(x, y)], end=' ')
        print()

def solve1(inp):
    cave = gen_cave(inp)
    floor = max(y for _, y in cave.keys())
    sand_cnt = 0
    while True:
        sx, sy = (500, 0)
        while True:
            if sy > floor:
                return sand_cnt
            if cave[(sx, sy + 1)] not in ("#", "o"):
                sy += 1
            elif cave[(sx - 1, sy + 1)] not in ("#", "o"):
                sx -= 1
                sy += 1
            elif cave[(sx + 1, sy + 1)] not in ("#", "o"):
                sx += 1
                sy += 1
            else:
                cave[(sx, sy)] = "o"
                sand_cnt += 1
                break
            

def solve2(inp):
    cave = gen_cave(inp)
    floor = max(y for _, y in cave.keys()) + 2
    sand_cnt = 0
    while True:
        sx, sy = (500, 0)
        while True:
            if cave[(500, 0)] == 'o':
                return sand_cnt
            if sy < floor and cave[sx, sy + 1] not in ("#", "o"):
                sy += 1
            elif sy < floor and cave[sx - 1, sy + 1] not in ("#", "o"):
                sx -= 1
                sy += 1
            elif sy < floor and cave[sx + 1, sy + 1] not in ("#", "o"):
                sx += 1
                sy += 1
            else:
                cave[sx, sy] = "o"
                sand_cnt += 1
                break

inp = puzzle_input("14")


print(solve1(inp))
print(solve2(inp))