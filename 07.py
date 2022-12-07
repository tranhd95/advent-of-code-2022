from collections import defaultdict

from utils import puzzle_input


def solve(inp):
    curr_dir = ("/",)
    fs = defaultdict(int)
    for line in inp.split("\n"):
        if line.startswith("dir") or line.startswith("ls"):
            continue
        elif line.startswith("$"):
            chunks = line.split(" ")
            cmd = chunks[1]
            if cmd == "cd":
                arg = chunks[2]
                if arg == "..":
                    curr_dir = curr_dir[:-1]
                elif arg == "/":
                    curr_dir = ("/",)
                else:
                    curr_dir = curr_dir + (arg,)
        else:
            size, _ = line.split(" ")
            size = int(size)
            fs[curr_dir] += size
            for i in range(1, len(curr_dir)):
                fs[curr_dir[:-i]] += size
    unused = 70_000_000 - fs[("/",)]
    need = 30_000_000
    print(sum(size for size in fs.values() if size <= 100_000))
    print(next(size for size in sorted(fs.values()) if (unused + size) >= need))


solve(puzzle_input("7"))
