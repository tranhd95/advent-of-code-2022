import re

from collections import namedtuple

from utils import puzzle_input

Instruction = namedtuple("Instruction", "n frm to")
re_numbers = re.compile(r"[0-9]+")


def parse(inp):
    crates_raw, instructions_raw = inp.split("\n\n")
    crates_lines = crates_raw.split("\n")
    stacks = []
    for col_idx in range(1, len(crates_lines[-1]), 4):
        crates = [crate for row in reversed(crates_lines[:-1]) if (crate := row[col_idx].strip())]
        stacks.append(crates)
    instructions = []
    for line in instructions_raw.split("\n"):
        numbers = map(int, re_numbers.findall(line))
        instructions.append(Instruction(*numbers))
    return stacks, instructions


def solve1(inp):
    crates, instructions = parse(inp)
    for ins in instructions:
        for _ in range(ins.n):
            to_be_moved = crates[ins.frm - 1].pop()
            crates[ins.to - 1].append(to_be_moved)
    print("".join([col.pop() for col in crates]))


def solve2(inp):
    crates, instructions = parse(inp)
    for ins in instructions:
        to_be_moved = crates[ins.frm - 1][-ins.n :]
        crates[ins.frm - 1] = crates[ins.frm - 1][: -ins.n]
        crates[ins.to - 1] += to_be_moved
    print("".join([col.pop() for col in crates]))


solve1(puzzle_input("5"))
solve2(puzzle_input("5"))
