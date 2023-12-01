#!/usr/bin/env python3

import sys

numbers = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

def import_challenge_data(path):
    with open(path, "r") as raw_data:
        return raw_data.readlines()

def get_first_digit(line):
    for char in line:
        if char.isdigit():
            return char

def get_last_digit(line):
    for char in line[::-1]:
        if char.isdigit():
            return char

def get_first_number(line):
    for i, char in enumerate(line):
        if char.isdigit():
            return char
        for k,v in numbers.items():
            if line[i:].startswith(v):
                return str(k)

def get_last_number(line):
    for i, char in enumerate(line[::-1]):
        if char.isdigit():
            return char
        j = (i * -1) + len(line) - 1
        for k,v in numbers.items():
            #print(f"{line=} {i=} {j=} {char=} {k=} {v=}")
            if line[j:].startswith(v):
                return str(k)            

def part_one(data):

    total = 0
    for line in data:
        first = get_first_digit(line)
        last = get_last_digit(line)
        calibration = int(first + last)
        total += calibration

    print(f"total = {total}")

def part_two(data):

    #i = 0

    total = 0
    for line in data:
        first = get_first_number(line.strip())
        last = get_last_number(line.strip())
        calibration = int(first + last)
        total += calibration
        #print(f"{i}: {total=}, {calibration=}")
        #if i > 10:
        #    sys.exit()
        #i += 1

    print(f"total = {total}")

def main():
    challenge_data = import_challenge_data("day01.txt")

    part_one(challenge_data)
    part_two(challenge_data)


if __name__ == "__main__":
    main()

