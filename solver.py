#!/usr/bin/env python3
""" Load daily challenges and display results. """

import argparse
from pathlib import Path

from rich import console as rcon

console = rcon.Console()

from dailies import day01, day02, day03, day04, day05, day06, day07, day08, day09, day10


def import_challenge_data(path: Path) -> list[str]:
    """Open challenge data and return as a list of lines."""
    with open(path, "r", encoding="utf-8") as raw_data:
        return raw_data.readlines()


def main(days: list[int] | None, samples: bool):
    """Display results for each challenge."""

    all_challenges = {
        1: day01,
        2: day02,
        3: day03,
        4: day04,
        5: day05,
        6: day06,
        7: day07,
        8: day08,
        9: day09,
        10: day10,
    }
    challenges = []

    if days:
        # User over-rode the default of displaying all
        for index in days:
            challenges.append((index, all_challenges[index]))
    else:
        challenges = all_challenges.items()

    for i, day in challenges:

        if samples:
            # the smaller example data sets
            data_source = Path("data") / f"sample{i:02}.txt"
        else:
            data_source = Path("data") / f"day{i:02}.txt"
        challenge_data = import_challenge_data(data_source)
        # TODO: inconsistent edge case where Day 1 has different sample data for Part 1 and Part 2
        #   Day 8 also has multiple sample data sets
        one = day.part_one(challenge_data)
        two = day.part_two(challenge_data)

        console.print(f"--- [style align right]Day {i}: {day.TITLE} ---")
        console.print(f"Part One: {one}")
        console.print(f"Part Two: {two}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--days", type=int, nargs="+", help="Only run the specified day(s)"
    )
    parser.add_argument(
        "--samples",
        action="store_true",
        help="Use smaller sample data instead of challenge data",
    )
    args = parser.parse_args()
    main(args.days, args.samples)
