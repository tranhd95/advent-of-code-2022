from utils import puzzle_input


def solve(string, n_distinct):
    i = n_distinct-1
    while len(set(string[i-n_distinct:i])) != n_distinct:
        i += 1
    print(i)

solve(puzzle_input("6"), 4)
solve(puzzle_input("6"), 14)