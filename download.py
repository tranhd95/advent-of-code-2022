#!/usr/bin/env python
import os
import sys

import requests

from dotenv import load_dotenv


def download_input(day, year=2022, suffix="in"):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    load_dotenv()
    req = requests.get(
        url,
        cookies={"session": os.getenv("COOKIE")},
        headers={
            "User-Agent": "github.com/tranhd95/advent-of-code-2022/ by tranhd95 _at_ gmail.com"
        },
    )
    if req.status_code != 200:
        raise Exception(req.content.decode("utf-8"))
    fname = f"data/{str(day).zfill(2)}.{suffix}"
    print(f"Saving {fname}...")
    save_file(req.content.decode("utf-8"), fname)


def save_file(content, filename):
    with open(filename, "w") as f:
        f.write(content)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid arguments", sys.argv)
        exit()
    day = sys.argv[1]
    download_input(day)
