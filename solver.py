#!/usr/bin/env python3
""" Load daily challenges and display results. """

from pathlib import Path
from dailies import day01, day02, day03, day04


def import_challenge_data(path: Path) -> list[str]:
    """Open challenge data and return as a list of lines."""
    with open(path, "r", encoding="utf-8") as raw_data:
        return raw_data.readlines()


def main():
    """Display results for each challenge."""

    challenges = [day01, day02, day03, day04]

    for i, day in enumerate(challenges, 1):
        # TODO: format string for leading zero
        data_source = Path("data") / f"day0{i}.txt"
        challenge_data = import_challenge_data(data_source)
        one = day.part_one(challenge_data)
        two = day.part_two(challenge_data)

        print(f"--- Day {i}: {day.TITLE} ---")
        print(f"Part One: {one}")
        print(f"Part Two: {two}\n")

        # Correct answers... for if I write unit tests
        # Day 01    54953, 53868
        # Day 02    2416, 63307
        # Day 03    544664, 84495585
        # Day 04    26426, 6227972


if __name__ == "__main__":
    main()
