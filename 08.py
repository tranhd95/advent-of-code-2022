import numpy as np

from utils import puzzle_input


def is_visible(matrix, row, col):
    height = matrix[row][col]
    is_taller = matrix < height
    dirs = (
        is_taller[:, col][:row],
        is_taller[:, col][row + 1 :],
        is_taller[row][:col],
        is_taller[row][col + 1 :],
    )
    return any(map(np.all, dirs))


def solve1(inp):
    matrix = np.array([list(map(int, list(line))) for line in inp.split("\n")])
    visible = 0
    for row in range(1, len(matrix) - 1):
        for col in range(1, len(matrix[0]) - 1):
            visible += int(is_visible(matrix, row, col))
    print(visible + sum(matrix.shape * 2) - 4)


def get_scenic_score(matrix, row, col):
    height = matrix[row][col]
    vertical = matrix[:, col]
    horizontal = matrix[row]
    dirs = (
        vertical[:row][::-1],
        vertical[row + 1 :],
        horizontal[:col][::-1],
        horizontal[col + 1 :],
    )
    score = 1
    for dir in dirs:
        can_see = next((cnt for cnt, h in enumerate(dir, start=1) if h >= height), len(dir))
        score *= can_see
    return score


def solve2(inp):
    matrix = np.array([list(map(int, list(line))) for line in inp.split("\n")])
    max_scenic_score = -1
    for row in range(1, len(matrix) - 1):
        for col in range(1, len(matrix[0]) - 1):
            max_scenic_score = max(max_scenic_score, get_scenic_score(matrix, row, col))
    print(max_scenic_score)


solve1(puzzle_input("8"))
solve2(puzzle_input("8"))
