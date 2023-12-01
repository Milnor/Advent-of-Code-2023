#!/usr/bin/env python3
""" Functions to solve the Day One challenges. """

numbers = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}


def get_first_digit(line):
    """ Return the first digit to occur in the line. """
    for char in line:
        if char.isdigit():
            return char
    raise ValueError("Digit not found")


def get_last_digit(line):
    """ Return the last digit to occur in the line. """
    for char in line[::-1]:
        if char.isdigit():
            return char
    raise ValueError("Digit not found")


def get_first_number(line):
    """ Return the first digit or number string to occur in the line. """
    for i, char in enumerate(line):
        if char.isdigit():
            return char
        for digit, number in numbers.items():
            if line[i:].startswith(number):
                return str(digit)
    raise ValueError("Number not found")


def get_last_number(line):
    """ Return the last digit or number string to occur in the line. """
    for i, char in enumerate(line[::-1]):
        if char.isdigit():
            return char
        # convert negative index to positive equivalent
        j = (i * -1) + len(line) - 1
        for digit, number in numbers.items():
            if line[j:].startswith(number):
                return str(digit)
    raise ValueError("Number not found")


def part_one(data):
    """ Calculate the results for Part One. """
    total = 0
    for line in data:
        first = get_first_digit(line)
        last = get_last_digit(line)
        calibration = int(first + last)
        total += calibration

    return total


def part_two(data):
    """ Calculate the results for Part Two. """
    total = 0
    for line in data:
        first = get_first_number(line.strip())
        last = get_last_number(line.strip())
        calibration = int(first + last)
        total += calibration

    return total
