import re
from utils import puzzle_input
from functools import lru_cache

re_nums = re.compile(r"(-*\d+)")
def parse_input(inp):
    sensors, beacons = [], []
    for line in inp.split("\n"):
        sx, sy, bx, by = tuple(map(int, re_nums.findall(line)))
        sensors.append((sx, sy))
        beacons.append((bx, by))
    return sensors, beacons

@lru_cache
def manhattan(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

def solve1(sensors, beacons, row):
    cnt = 0
    beacons_set = set(beacons)
    xmin, xmax = min(sx for sx, _ in beacons), max(sx for sx, _ in beacons)
    for x in range(xmin, xmax+1):
        for (sx, sy), b in zip(sensors, beacons):
            radius = manhattan(sx, sy, *b)
            if manhattan(x, row, sx, sy) <= radius and (x, row) not in beacons_set:
                cnt += 1
                break
    return cnt

def solve2(sensors, beacons, bound):
    for x in range(bound+1):
        y = 0
        while y < bound:
            for (sx, sy), b in zip(sensors, beacons):
                radius = manhattan(sx, sy, *b)
                if (dist := manhattan(x, y, sx, sy)) <= radius:
                    y += radius - dist
                    break
            else:
                return (x * 4_000_000 + y)
            y += 1

print(solve1(*parse_input(puzzle_input("15")), row=2_000_000))
print(solve2(*parse_input(puzzle_input("15")), bound=4_000_000))
