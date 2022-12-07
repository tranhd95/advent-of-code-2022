from collections import defaultdict

from utils import puzzle_input


def solve(inp):
    curr_dir = ("/",)
    fs = defaultdict(int)
    for line in inp.split("\n"):
        match line.split(" "):
            case ["dir", _] | ["$", "ls"]:
                continue
            case ["$", "cd", ".."]:
                curr_dir = curr_dir[:-1]
            case ["$", "cd", "/"]:
                curr_dir = ("/",)
            case ["$", "cd", dest]:
                curr_dir = curr_dir + (dest,)
            case [size, _]:
                size = int(size)
                fs[curr_dir] += size
                for i in range(1, len(curr_dir)):
                    fs[curr_dir[:-i]] += size
    unused = 70_000_000 - fs[("/",)]
    need = 30_000_000
    sizes = sorted(fs.values())
    print(sum(s for s in sizes if s <= 100_000))
    print(next(s for s in sizes if (unused + s) >= need))


solve(puzzle_input("7"))
