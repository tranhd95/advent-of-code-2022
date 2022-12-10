from utils import puzzle_input

DIRS = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}


def sign(x):
    if x == 0:
        return 0
    return 1 if x > 0 else -1


def solve(inp, n=10):
    knots = [(0, 0) for _ in range(n)]
    seen = {(0, 0)}
    for line in inp.split("\n"):
        dir, steps = line.split(" ")

        for _ in range(int(steps)):
            hx, hy = knots[0]
            dx, dy = DIRS[dir]
            knots[0] = hx + dx, hy + dy
            for i in range(len(knots) - 1):
                hx, hy = knots[i]
                tx, ty = knots[i + 1]
                dx, dy = hx - tx, hy - ty
                if dx ** 2 + dy ** 2 > 2:
                    knots[i + 1] = (tx + sign(dx), ty + sign(dy))
            seen.add(knots[-1])
    print(len(seen))


solve(puzzle_input("9"), 2)
solve(puzzle_input("9"), 10)
