#!/usr/bin/env python3
""" Functions to solve the Day Two challenges. """

from dataclasses import dataclass

TITLE = "Cube Conundrum"


@dataclass
class GameSet:
    """One set of cubes from the knapsack."""

    red: int
    green: int
    blue: int


def calculate_power(sets: list[GameSet]) -> int:
    """Calculate the power of the minimal set."""
    r_min = 0
    g_min = 0
    b_min = 0

    for each in sets:
        if each.red > r_min:
            r_min = each.red
        if each.green > g_min:
            g_min = each.green
        if each.blue > b_min:
            b_min = each.blue

    return r_min * g_min * b_min


def all_sets_good(sets: list[GameSet]) -> bool:
    """True if no set of game data in list exceeds parameters."""
    for each in sets:
        if each.red > 12:
            return False
        if each.green > 13:
            return False
        if each.blue > 14:
            return False

    return True


def parse_set(data: str) -> GameSet:
    """Parse out GameSet from string."""

    red = 0
    green = 0
    blue = 0
    chunks = data.split(",")

    for chunk in chunks:
        number, color = chunk.strip().split(" ")
        if "red" in color:
            red = int(number)
        elif "green" in color:
            green = int(number)
        elif "blue" in color:
            blue = int(number)
        else:
            raise ValueError("Bad set data")

    return GameSet(red=red, green=green, blue=blue)


def parse_game(line: str) -> tuple[int, list[GameSet]]:
    """Parse out Game ID and multiple sets of cubes."""

    sets = []
    game, set_data = line.split(":")
    game_id = int(game[5:])

    for each in set_data.strip().split(";"):
        sets.append(parse_set(each))

    return game_id, sets


def part_one(data: list[str]) -> int:
    """Calculate the results for Part One."""

    total = 0

    for line in data:
        game_id, sets = parse_game(line)
        if all_sets_good(sets):
            total += game_id

    return total


def part_two(data: list[str]) -> int:
    """Calculate the results for Part Two."""

    total = 0

    for line in data:
        _, sets = parse_game(line)
        total += calculate_power(sets)

    return total
