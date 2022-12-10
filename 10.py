from utils import puzzle_input


def determine_symbol(cycle, sprite_idx):
    if sprite_idx <= cycle % 40 <= sprite_idx + 2:
        return "▓"
    else:
        return "░"


def solve(inp):
    cycle = 1
    X = 1
    total_strength = 0
    for line in inp.split("\n"):
        print(determine_symbol(cycle, X), end="")
        cycle += 1
        chunks = line.split(" ")

        if chunks[0] == "addx":
            if cycle % 40 == 20:
                total_strength += cycle * X
            elif cycle % 40 == 1:
                print()
            print(determine_symbol(cycle, X), end="")
            cycle += 1
            X += int(chunks[1])

        if cycle % 40 == 20:
            total_strength += cycle * X
        elif cycle % 40 == 1:
            print()

    print(total_strength)


solve(puzzle_input("10"))
