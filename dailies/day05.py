#!/usr/bin/env python3
""" Functions to solve the Day Five challenges. """

TITLE = "If You Give A Seed A Fertilizer"

def generate_mappings(line: str) -> list[tuple[int, int]]:
    """Convert sequence of digits to list source-dest mapping tuples."""
    pass # check that type hint is correct

def part_one(data: list[str]) -> int:
    """Calculate the results for Part One."""

    total = 0
    seeds = [] # ints
    seed_to_soil = [] # tuples... maybe? Or change to dictionary?
    current_map = None

    for line in data:
        if line.startswith("seeds"):
            # values are on the same line
            _, digits  = line.split(':')
            seeds = digits.split()
        elif line.startswith("seed-to-soil map"):
            # arbitrary number of lines with digits
            current_map = seed_to_soil
        elif line.startswith("soil-to-fertilizer map"):
            current_map = soil_to_fertilizer
        elif line.startswith("fertilizer-to-water map"):
            current_map = fertilizer_to_water
        elif line.startswith("water-to-light map"):
            current_map = water_to_light
        elif line.startswith("light-to-temperature map"):
            current_map = light_to_temp
        elif line.startswith("temperature-to-humidity"):
            current_map = temp_to_humidity
        elif line.startswith("humidity-to-location map"):
            current_map = humidity_to_location
        elif line[0].isdigit():
            current_map.extend(generate_mappings(line))
        

    print(f"{seeds}")

    return total


def part_two(data: list[str]) -> int:
    """Calculate the results for Part Two."""

    total = 0

    # TBD...

    return total
