from dataclasses import dataclass
from math import lcm, prod
from typing import Callable

from utils import puzzle_input


@dataclass
class Monkey:
    items: list[int]
    operation: Callable[[int], int]
    test: int
    true: int
    false: int
    inspections = 0


def iter_monkeys_from_input(inp):
    for raw_monkey in inp.split("\n\n"):
        lines = raw_monkey.split("\n")
        items = eval(f"[{lines[1].split(':')[-1]}]")
        operation = eval(lines[2].split(":")[-1].replace("new =", "lambda old:"))
        test = int(lines[3].split(" ")[-1])
        true = int(lines[4].split(" ")[-1])
        false = int(lines[5].split(" ")[-1])
        yield Monkey(items, operation, test, true, false)


def solve1(inp):
    monkeys = list(iter_monkeys_from_input(inp))
    for _ in range(20):
        for monkey in monkeys:
            while monkey.items:
                monkey.inspections += 1
                worry_level = monkey.operation(monkey.items.pop()) // 3
                target = monkey.true if worry_level % monkey.test == 0 else monkey.false
                monkeys[target].items.append(worry_level)
    print(prod(sorted(monkey.inspections for monkey in monkeys)[-2:]))


def solve2(inp):
    monkeys = list(iter_monkeys_from_input(inp))
    lcm_ = lcm(*(monkey.test for monkey in monkeys))
    for _ in range(10_000):
        for monkey in monkeys:
            while monkey.items:
                monkey.inspections += 1
                worry_level = monkey.operation(monkey.items.pop())
                worry_level %= lcm_
                target = monkey.true if worry_level % monkey.test == 0 else monkey.false
                monkeys[target].items.append(worry_level)
    print(prod(sorted(monkey.inspections for monkey in monkeys)[-2:]))


inp = puzzle_input("11")
solve1(inp)
solve2(inp)
