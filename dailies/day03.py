#!/usr/bin/env python3
""" Functions to solve the Day Three challenges. """

from dataclasses import dataclass

TITLE = "Gear Ratios"

@dataclass
class Number:
    """May or may not be a part number."""
    value: int
    row: int
    start_col: int
    end_col: int
    part_number: bool

@dataclass
class Gear:
    """May or may not be an actual gear."""
    row: int
    col: int
    numbers: list[int]
    gear: bool

# game_board and numbers were originally local to part_one()
game_board = {}
numbers = []
gears = []

def collides(gear: Gear, number: Number):
    """Return true if gear falls within number's collision rectangle."""
    #upper_left = number.start_col - 1, number.row - 1
    #lower_right = number.end_col + 1, number.row + 1
    # no bounds checking because we can ignore the actual game_board
    if gear.row >= number.row - 1 and gear.row <= number.row + 1 and gear.col >= number.start_col - 1 and gear.col <= number.end_col + 1:
        return True

def populate_gear_adjacencies():
    """Determine which potential gears are adjacent to exactly two numbers."""
    
    for gear in gears:
        # add each number adjacent
        for number in numbers:
            if collides(gear, number):
                gear.numbers.append(number.value)

        # make as gear if exactly two numbers
        if len(gear.numbers) == 2:
            gear.gear = True

def is_part_number(number: Number, game_board: dict) -> bool:
    """Check adjacent rows/columns for symbols to determine whether number is a part number."""

    # check row above
    if number.row - 1 in game_board.keys():
        start = number.start_col - 1 if number.start_col > 0 else 0
        end = number.end_col + 1 if number.end_col < len(game_board[number.row]) - 1 else number.end_col
        for char in game_board[number.row - 1][start:end+1]:
            if not char.isdigit() and char != '.':
                # found an adjacent symbol
                print(f"{number.value} at line 27")
                return True

    # check row where number occurs
    if number.start_col > 0:
        previous = game_board[number.row][number.start_col - 1]
        if not previous.isdigit() and previous != '.':
            # found an adjacent symbol
            print(f"{number.value} at line 35")
            return True
    if number.end_col < len(game_board[number.row]) - 2:
        next = game_board[number.row][number.end_col + 1]
        if not next.isdigit() and next != '.':
            # found an adjacent symbol
            print(f"{number.value} at line 41")
            return True

    # check row below
    if number.row + 1 in game_board.keys():
        start = number.start_col - 1 if number.start_col > 0 else 0
        end = number.end_col + 1 if number.end_col < len(game_board[number.row]) - 1 else number.end_col
        for char in game_board[number.row + 1][start:end+1]:
            if not char.isdigit() and char != '.':
                # found an adjacent symbol
                print(f"{number.value} at line 51")
                return True

    return False


def parse_numbers(line: str, row: int) -> list[Number]:
    """Generate a Number from each group of consecutive digits."""

    numbers = []
    indices = []
    current_num = ""

    for i, char in enumerate(line):
        if char.isdigit():
            current_num += char
            indices.append(i)
        else:
            if current_num != "":
                numbers.append(Number(value=int(current_num), row=row, start_col=indices[0], end_col=indices[-1], part_number=False))
                current_num = ""
                indices = []
            if char == '*':
                gears.append(Gear(row=row, col=i, numbers=[], gear=False))

    return numbers



def part_one(data: list[str]) -> int:
    """Calculate the results for Part One."""

    total = 0

    for i, line in enumerate(data):
        # add line to the game board
        game_board[i] = line.strip()

        # create Number for each set of digits and place in list
        numbers.extend(parse_numbers(line, i))

    # determine which are part numbers
    for number in numbers:
        if is_part_number(number, game_board):
            number.part_number = True

    for number in numbers:
        if number.part_number:
            total += number.value

    print(numbers)

    return total

# Note: operates on the assumption that part_one() was called first, populating globals
def part_two(data: list[str]) -> int:
    """Calculate the results for Part Two."""

    total = 0

    populate_gear_adjacencies()

    # calculate gear ratios
    for gear in gears:
        if gear.gear:
            total += (gear.numbers[0] * gear.numbers[1])

    return total
