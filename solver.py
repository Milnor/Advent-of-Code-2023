#!/usr/bin/env python3
""" Load daily challenges and display results. """

import argparse
from pathlib import Path

#from rich import print as rprint
from rich import console as rcon
console = rcon.Console()

from dailies import day01, day02, day03, day04, day05, day06, day07, day08, day09


def import_challenge_data(path: Path) -> list[str]:
    """Open challenge data and return as a list of lines."""
    with open(path, "r", encoding="utf-8") as raw_data:
        return raw_data.readlines()


def main(days: list[int] | None, samples: bool):
    """Display results for each challenge."""

    all_challenges = {1: day01, 2: day02, 3: day03, 4: day04, 5: day05, 6: day06, 7: day07, 8: day08, 9: day09}
    challenges = []

    if days:
        # User over-rode the default of displaying all
        for index in days:
            challenges.append((index, all_challenges[index]))
    else:
        challenges = [(k, v) for k, v in all_challenges.items()]

    for i, day in challenges:
        # TODO: format string for leading zero
        if samples:
            # the smaller example data sets
            data_source = Path("data") / f"sample0{i}.txt"
        else:
            data_source = Path("data") / f"day0{i}.txt"
        challenge_data = import_challenge_data(data_source)
        # TODO: inconsistent edge case where Day 1 has different sample data for Part 1 and Part 2
        #   Day 8 also has multiple sample data sets
        one = day.part_one(challenge_data)
        two = day.part_two(challenge_data)

        console.print(f"--- [style align right]Day {i}: {day.TITLE} ---")
        console.print(f"Part One: {one}")
        console.print(f"Part Two: {two}\n")

        # Correct answers... for if I write unit tests
        #           Challenge Data          Sample Data
        # Day 01    54953, 53868            142, 281
        # Day 02    2416, 63307             8, 2286
        # Day 03    544664, 84495585        4361, 467835
        # Day 04    26426, 6227972          13, 30
        # Day 05    579439039, tbd          35, 46
        # Day 06    500346, 42515755        288, 71503
        # Day 07    250120186, 250665248    6440, 5905
        # Day 08    21251, 11678319315857   2|6, 6
        # Day 09    2105961943, 1019        114, 2

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--days', type=int, nargs='+', help='Only run the specified day(s)')
    parser.add_argument('--samples', action='store_true', help='Use smaller sample data instead of challenge data')
    args = parser.parse_args()
    main(args.days, args.samples)
