#!/usr/bin/env python3
""" Functions to solve the Day Eight challenges. """

from math import lcm

TITLE = "Haunted Wasteland"

def parse_directions(data: str):
    """Parse out node name and its left/right values."""

    name, directions = data.split('=')
    name = name.strip()
    left, right = directions.strip().split(',')

    return name, left[1:], right[1:-1]


def get_direction(directions: str, index: int):
    """Get the next R|L direction."""
    #print(f"get_dir({directions},{index})")
    if index > 0:
        index = index % len(directions)
    return directions[index]

def check_for_done(currents: list[str], count: int):
    """Return True only if we've stored a count for when each item first ends in 'Z'."""

    done = True

    for each in currents:
        if each[1] == -1:
            if each[0].endswith('Z'):
                each[1] = count
            else:
                done = False

    #print("Success!!")
    return done

def part_one(data: list[str]) -> int:
    """Calculate the results for Part One."""

    total = 0
    nodes = {}
    instructions = ""
    current = 'AAA'

    for line in data:
        if line[0].isalpha() and '=' not in line:
            instructions = line.strip()
        elif '=' in line:
            key, left, right = parse_directions(line)
            #print(f"{key} {left} {right}")
            nodes[key] = (left, right)
        else:
            pass
    #print(f"instructions ==> \'{instructions}\'")
    while current != 'ZZZ':
        direction = get_direction(instructions, total)
        #print(f"{total=} {direction=}")
        if direction == 'L':
            current = nodes[current][0]
        elif direction == 'R':
            current = nodes[current][1]
        else:
            raise ValueError(f"Expected R|L, got {direction}")
        total += 1

    return total


def part_two(data: list[str]) -> int:
    """Calculate the results for Part Two."""
    #return -1
    total = 0
    nodes = {}
    instructions = ""
    #current = 'AAA'
    currents = []
    end_points = [] # debug only
    finished = False

    for line in data:
        if line[0].isalpha() and '=' not in line:
            instructions = line.strip()
        elif '=' in line:
            key, left, right = parse_directions(line)
            #print(f"{key} {left} {right}")
            nodes[key] = (left, right)
        else:
            pass
    #print(f"instructions ==> \'{instructions}\'")

    for each in nodes.keys():
        if each.endswith('A'):
            currents.append([each, -1])
        elif each.endswith('Z'):
            end_points.append(each)

    print(f"start_points: {currents}")
    print(f"end points: {end_points}")

    # Reddit suggested Least Common Multiple.
    # I didn't steal code, but I stole that epiphany.

    while not finished:

        direction = get_direction(instructions, total)
        for i, each in enumerate(currents):
            
            if direction == 'L':
                currents[i][0] = nodes[each[0]][0]
            elif direction == 'R':
                currents[i][0] = nodes[each[0]][1]
            else:
                raise ValueError(f"Expected R|L, got {direction}")
        total += 1
        
        #print(f"{total}: {currents}")
        finished = check_for_done(currents, total)
        if finished:
            print(currents)
    
    indices = [num for node, num in currents]

    return lcm(*indices)
