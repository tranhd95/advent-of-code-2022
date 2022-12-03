from utils import puzzle_input

scores = (
    (3, 0, 6),
    (6, 3, 0),
    (0, 6, 3)
)

scores2 = (
    (0 + 3, 0 + 1, 0 + 2),
    (3 + 1, 3 + 2, 3 + 3),
    (6 + 2, 6 + 3, 6 + 1)
)


def solve1(inp):
    total = 0
    for line in inp.split("\n"):
        opp, me = line.split(" ")
        opp = ord(opp) % ord("A")
        me = ord(me) % ord("X")
        total += scores[me][opp] + me + 1
    print(total)


def solve2(inp):
    total = 0
    for line in inp.split("\n"):
        opp, me = line.split(" ")
        opp = ord(opp) % ord("A")
        me = ord(me) % ord("X")
        total += scores2[me][opp]
    print(total)


solve1(puzzle_input("2"))
solve2(puzzle_input("2"))