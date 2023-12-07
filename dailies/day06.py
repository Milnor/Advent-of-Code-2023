#!/usr/bin/env python3
""" Functions to solve the Day Six challenges. """

TITLE = "Wait For It"

class Race:
    """Boat race times and distances to beat."""

    def __init__(self, time, distance):
        self.time = time
        self.distance = distance

    def __str__(self):
        return f"Race: time={self.time}, distance={self.distance}"
    
    def brute_force(self):
        """Only for small data sets to help visualize the problem."""
        for button_press in range(self.time + 1):
            total_dist = button_press * (self.time - button_press)
            print(f"{button_press} ms ==> {total_dist} mm")
    
    def ways_to_win(self) -> int:
        """Calculate the number of ways to beat the record distance."""
        min_to_win = None
        #max_to_win = None

        for button_press in range(self.time + 1):
            if not min_to_win:
                # Still looking for minimum button hold time
                if button_press * (self.time - button_press) > self.distance:
                    min_to_win = button_press
            else:
                # Detect the first loss and return
                if button_press * (self.time - button_press) <= self.distance:
                    return button_press - min_to_win

boat_races = []

def fix_kerning(text: str) -> int:
    """Remove spaces and build one big integer."""
    result = ""
    for char in text:
        if char.isdigit():
            result += char
    
    return int(result)

def parse_races(data: list[str]) -> list[Race]:
    """Parse boat races from lines of text."""
    times = []
    distances = []

    for line in data:
        if line.startswith("Time:"):
            _, nums = line.split(":")
            for value in nums.split():
                times.append(int(value))
        elif line.startswith("Distance:"):
            _, nums = line.split(":")
            for value in nums.split():
                distances.append(int(value))
        else:
            raise ValueError(f"Unexpected input: {line}")
    
    return [Race(time, distance) for time, distance in zip(times, distances)]

def part_one(data: list[str]) -> int:
    """Calculate the results for Part One."""

    ways_to_win = 1

    boat_races.extend(parse_races(data))
    for race in boat_races:
        #print(race.ways_to_win())
        ways_to_win *= race.ways_to_win()
    #boat_races[0].brute_force()

    return ways_to_win


def part_two(data: list[str]) -> int:
    """Calculate the results for Part Two."""

    for line in data:
        if line.startswith("Time:"):
            text, digits = line.split(":")
            time = fix_kerning(digits)
        elif line.startswith("Distance:"):
            text, digits = line.split(":")
            distance = fix_kerning(digits)
        else:
            raise ValueError(f"Unexpected input: {line}")
    
    single_race = Race(time, distance)

    return single_race.ways_to_win()
