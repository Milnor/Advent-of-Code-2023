#!/usr/bin/env python3
""" Functions to solve the Day Five challenges. """

TITLE = "If You Give A Seed A Fertilizer"

class Converter:
    """Stores lookup data to convert seed to soil, etc."""

    def __init__(self, name):
        self.name = name
        self.mappings = []
    
    def add_mapping(self, dest: int, source: int, length: int) -> None:
        """Add a dest, source, length tuple to self.mappings list."""
        self.mappings.append((source, dest, length))

    def lookup(self, input: int) -> int:
        """Convert seed to soil, soil to fertilizer, etc."""
        for src, dst, length in self.mappings:
            if input >= src and input <= src + length:
                #print(f"lookup({input}) --> {dst + (input - src)}")
                return dst + (input - src)
        
        # Or no explicit mapping exists
        return input
"""
def location_lookup(seed: int, **converters) -> int:
    #Find the location of a seed.
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
"""

def generate_seeds(line: str) -> list[int]:
    """Create list of start_value, length pairs."""
    output = []
    # values are on the same line
    _, digits  = line.split(':')
    str_seeds = digits.split()
    int_seeds = [int(i) for i in str_seeds]
    # Now they need to be converted into start, length pairs
    for i, value in enumerate(int_seeds):
        #start = None
        #length = None
        if i % 2 == 0:
            start = value
        else:
            length = value
            output.append((start, length))
    return output

def location_lookup(seed: int, converters: list[Converter]):
    """Find the location of a seed."""
    soil = converters["soil"].lookup(seed)
    fertilizer = converters["fertilizer"].lookup(soil)
    water = converters["water"].lookup(fertilizer)
    light = converters["light"].lookup(water)
    temperature = converters["temperature"].lookup(light)
    humdity = converters["humidity"].lookup(temperature)
    location = converters["location"].lookup(humdity)
    #print(f"{seed=} {soil=} {fertilizer=} {water=} {light=} {temperature=} {humdity=} {location=}")
    return location

def part_one(data: list[str]) -> int:
    """Calculate the results for Part One."""

    seeds = [] # ints
    converters = {} # Converters
    """
    seed_to_soil = {} # int: int
    soil_to_fertilizer = {}
    fertilizer_to_water = {}
    water_to_light = {}
    light_to_temp = {}
    temp_to_humidity = {}
    humidity_to_location = {}
    """
    current_map = None

    for line in data:
        if line.startswith("seeds"):
            # values are on the same line
            _, digits  = line.split(':')
            raw_seeds = digits.split()
            seeds = [int(i) for i in raw_seeds]
        elif line.startswith("seed-to-soil map"):
            # arbitrary number of lines with digits
            current_map = Converter("seed-to-soil")
            converters["soil"] = current_map
        elif line.startswith("soil-to-fertilizer map"):
            current_map = Converter("soil-to-fertilizer")
            converters["fertilizer"] = current_map
        elif line.startswith("fertilizer-to-water map"):
            current_map = Converter("fertilizer-to-water")
            converters["water"] = current_map
        elif line.startswith("water-to-light map"):
            current_map = Converter("water-to-light")
            converters["light"] = current_map
        elif line.startswith("light-to-temperature map"):
            current_map = Converter("light-to-temperature")
            converters["temperature"] = current_map
        elif line.startswith("temperature-to-humidity"):
            current_map = Converter("temperatore-to-humidity")
            converters["humidity"] = current_map
        elif line.startswith("humidity-to-location map"):
            current_map = Converter("humidity-to-location")
            converters["location"] = current_map
        elif line[0].isdigit():
            # Order is destination, source, length
            dst, src, length = line.split()
            #for i in range(int(length)):
            #    current_map[int(src) + i] = int(dst) + i
            current_map.add_mapping(int(dst), int(src), int(length))
        elif line[0] == '\n':
            pass # ignore newlines
        else:
            raise ValueError(f"Unexpected value: {line}")
    
    lowest = None
    for seed in seeds:
        """
        location = location_lookup(seed, 
                                   seed_to_soil=seed_to_soil,
                                   soil_to_fertilizer=soil_to_fertilizer,
                                   fertilizer_to_water=fertilizer_to_water,
                                   water_to_light=water_to_light,
                                   light_to_temp=light_to_temp,
                                   temp_to_humidity=temp_to_humidity,
                                   humidity_to_location=humidity_to_location)
        """
        location = location_lookup(seed, converters)
        #print(f"{location=}, {lowest=}")
        if not lowest:
            lowest = location
        elif lowest and location < lowest:
            lowest = location
    
    #print(seeds)
    #print(type(seeds[0]))

    return lowest

# should refactor to eliminate code duplication with part_one()
def part_two(data: list[str]) -> int:
    """Calculate the results for Part Two."""

    return -1 # TODO: fix this mess that takes 7.6 hours to run and still gives the wrong answer

    #--- Day 5: If You Give A Seed A Fertilizer ---
    #Part One: 579439039
    #Part Two: 7873085


    #real    456m7.714s
    #user    198m52.878s
    #sys     1m56.678s

    seeds = [] # ints
    converters = {} # Converters
    current_map = None

    for line in data:
        if line.startswith("seeds"):
            seeds = generate_seeds(line)
        elif line.startswith("seed-to-soil map"):
            # arbitrary number of lines with digits
            current_map = Converter("seed-to-soil")
            converters["soil"] = current_map
        elif line.startswith("soil-to-fertilizer map"):
            current_map = Converter("soil-to-fertilizer")
            converters["fertilizer"] = current_map
        elif line.startswith("fertilizer-to-water map"):
            current_map = Converter("fertilizer-to-water")
            converters["water"] = current_map
        elif line.startswith("water-to-light map"):
            current_map = Converter("water-to-light")
            converters["light"] = current_map
        elif line.startswith("light-to-temperature map"):
            current_map = Converter("light-to-temperature")
            converters["temperature"] = current_map
        elif line.startswith("temperature-to-humidity"):
            current_map = Converter("temperatore-to-humidity")
            converters["humidity"] = current_map
        elif line.startswith("humidity-to-location map"):
            current_map = Converter("humidity-to-location")
            converters["location"] = current_map
        elif line[0].isdigit():
            # Order is destination, source, length
            dst, src, length = line.split()
            #for i in range(int(length)):
            #    current_map[int(src) + i] = int(dst) + i
            current_map.add_mapping(int(dst), int(src), int(length))
        elif line[0] == '\n':
            pass # ignore newlines
        else:
            raise ValueError(f"Unexpected value: {line}")
    
    lowest = None
    #print(f"{seeds=}")
    #import sys
    #sys.exit()
    #for seed in seeds:
    """
        location = location_lookup(seed, 
                                   seed_to_soil=seed_to_soil,
                                   soil_to_fertilizer=soil_to_fertilizer,
                                   fertilizer_to_water=fertilizer_to_water,
                                   water_to_light=water_to_light,
                                   light_to_temp=light_to_temp,
                                   temp_to_humidity=temp_to_humidity,
                                   humidity_to_location=humidity_to_location)
    """
    for start, length in seeds:
        print(f"inside outer loop where {start=}")

        for seed in range(start, (start + length) - 1):
            #print(f"inside loop: ")
            location = location_lookup(seed, converters)
            #print(f"{location=}, {lowest=}")
            if not lowest:
                lowest = location
            elif lowest and location < lowest:
                lowest = location
    
    print(seeds)
    print(type(seeds[0]))

    return lowest
