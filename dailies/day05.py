#!/usr/bin/env python3
""" Functions to solve the Day Five challenges. """

TITLE = "If You Give A Seed A Fertilizer"

def location_lookup(seed: int, **converters) -> int:
    """Find the location of a seed."""
    #print(kwargs)
    soil = converters["seed_to_soil"][seed] if seed in converters["seed_to_soil"].keys() else seed
    fertilizer = converters["soil_to_fertilizer"][soil] if soil in converters["soil_to_fertilizer"].keys()  else soil
    water = converters["fertilizer_to_water"][fertilizer] if fertilizer in converters["fertilizer_to_water"].keys() else fertilizer
    light = converters["water_to_light"][water] if water in converters["water_to_light"].keys() else water
    temp = converters["light_to_temp"][light] if light in converters["light_to_temp"].keys() else light
    humdity = converters["temp_to_humidity"][temp] if temp in converters["temp_to_humidity"].keys() else temp
    location = converters["humidity_to_location"][humdity] if humdity in converters["humidity_to_location"].keys() else humdity
    print(f"{seed=} {soil=} {fertilizer=} {water=} {light=} {temp=} {humdity=} {location=}")
    return location

def part_one(data: list[str]) -> int:
    """Calculate the results for Part One."""

    seeds = [] # ints
    seed_to_soil = {} # int: int
    soil_to_fertilizer = {}
    fertilizer_to_water = {}
    water_to_light = {}
    light_to_temp = {}
    temp_to_humidity = {}
    humidity_to_location = {}

    current_map = None

    for line in data:
        if line.startswith("seeds"):
            # values are on the same line
            _, digits  = line.split(':')
            raw_seeds = digits.split()
            seeds = [int(i) for i in raw_seeds]
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
            # Order is destination, source, length
            dst, src, length = line.split()
            for i in range(int(length)):
                current_map[int(src) + i] = int(dst) + i
        elif line[0] == '\n':
            pass # ignore newlines
        else:
            raise ValueError(f"Unexpected value: {line}")
    
    lowest = None
    for seed in seeds:
        location = location_lookup(seed, 
                                   seed_to_soil=seed_to_soil,
                                   soil_to_fertilizer=soil_to_fertilizer,
                                   fertilizer_to_water=fertilizer_to_water,
                                   water_to_light=water_to_light,
                                   light_to_temp=light_to_temp,
                                   temp_to_humidity=temp_to_humidity,
                                   humidity_to_location=humidity_to_location)
        print(f"{location=}, {lowest=}")
        if not lowest:
            lowest = location
        elif lowest and location < lowest:
            lowest = location
    
    print(seeds)
    print(type(seeds[0]))

    return lowest


def part_two(data: list[str]) -> int:
    """Calculate the results for Part Two."""

    total = 0

    # TBD...

    return total
