import fileinput
import os

from download import download_input

YEAR = 2022


def iter_lines(inp):
    for line in inp.split("\n"):
        if line:
            yield line


def iter_file(day, year=YEAR):
    fname = f"data/{str(day).zfill(2)}.in"
    if not os.path.exists(fname):
        download_input(day, year)
    with fileinput.input(fname) as f:
        for line in f:
            yield line.strip()


def puzzle_input(day, year=YEAR):
    fname = f"data/{str(day).zfill(2)}.in"
    if not os.path.exists(fname):
        download_input(day, year)
    with open(fname, "r") as f:
        return f.read().rstrip()
