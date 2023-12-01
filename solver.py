#!/usr/bin/env python3
""" Load daily challenges and display results. """

from dailies import day01


def import_challenge_data(path):
    """ Open challenge data and return as a list of lines. """
    with open(path, "r", encoding="utf-8") as raw_data:
        return raw_data.readlines()


def main():
    """ Display results for each challenge. """

    challenge_data = import_challenge_data("data/day01.txt")

    one = day01.part_one(challenge_data)  # correct answer was 54953
    two = day01.part_two(challenge_data)  # correct answer was 53868

    print("--- Day 1: Trebuchet?! ---")
    print(f"Part One: {one}")
    print(f"Part Two: {two}")


if __name__ == "__main__":
    main()
