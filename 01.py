from utils import puzzle_input


def solve(inp, top_n):
    totals = []
    for chunk in inp.split("\n\n"):
        chunks = chunk.split("\n")
        s = sum(map(int, chunks))
        totals.append(s)
    print(sum(sorted(totals, reverse=True)[:top_n]))


solve(puzzle_input("1"), top_n=1)
solve(puzzle_input("1"), top_n=3)