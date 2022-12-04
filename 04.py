from utils import puzzle_input


def solve(inp):
    fully_contains, overlaps = 0, 0
    for line in inp.split("\n"):
        fst, snd = line.split(",")
        fst_from, fst_to = tuple(map(int, fst.split("-")))
        snd_from, snd_to = tuple(map(int, snd.split("-")))
        fst_range = set(range(fst_from, fst_to+1))
        snd_range = set(range(snd_from, snd_to+1))
        if fst_range <= snd_range or snd_range <= fst_range:
            fully_contains += 1
        if set(fst_range) & set(snd_range):
            overlaps += 1
    print(fully_contains)
    print(overlaps)

solve(puzzle_input("4"))