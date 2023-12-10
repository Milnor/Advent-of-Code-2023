#!/usr/bin/env python3
""" Functions to solve the Day Nine challenges. """

TITLE = "Mirage Maintenance"

class Sequence:
    """A list of integers with tools to calculate next in sequence."""

    def __init__(self, numbers: list[int]):
        self.numbers = numbers
        self.depth = self.calculate_deltas()
        #self.depth = None       # layers until all zeroes
        self.next = self.calculate_next()   # next value in sequence
        self.prev = self.calculate_prev()   # previous value in sequence

    def __str__(self):
        return f"numbers={self.numbers} depth={self.depth} next={self.next}"
    
    def calculate_deltas(self) -> int:
        """Build list of lists of deltas; return depth to all zeroes."""
        print("got here")
        self.deltas = []
        current = self.numbers
        while self.non_zero(current):
            print("got here too")
            diffs = []
            previous = current[0]
            for i in range(1, len(current)):
                diffs.append(current[i] - previous)
                previous = current[i]
            self.deltas.append(diffs)
            current = diffs
            print(f"{diffs=}")
        return len(self.deltas)

    def non_zero(self, numbers: list[int]):
        """Return False if every element is 0, True otherwise."""
        print("inside non_zero")
        for element in numbers:
            if element != 0:
                return True
        return False

    def calculate_next(self) -> int:
        """Return next integer in sequence."""

        last = 0
        for sublist in reversed(self.deltas):
            sublist.append(sublist[-1] + last)
            last = sublist[-1]
        
        return self.numbers[-1] + self.deltas[0][-1]

    def calculate_prev(self) -> int:
        """Return previous integer in sequence."""

        # This is less intuitive than calculate_next(), because it is
        # the distance between the two points rather than the sum.

        last = 0
        for sublist in reversed(self.deltas):
            prev = sublist[0] - last
            sublist.insert(0, prev)
            last = sublist[0]
        
        return self.numbers[0] - self.deltas[0][0]

sequences = []        

def part_one(data: list[str]) -> int:
    """Calculate the results for Part One."""

    total = 0
    
    for line in data:
        numbers = line.strip().split()
        sequences.append(Sequence([int(i) for i in numbers]))

    for sequence in sequences:
        total += sequence.next

    print(f"{sequences[0]}\n{sequences[1]}\n{sequences[2]}")

    return total

# Note: Assumes Part One was already called to populate sequences
def part_two(data: list[str]) -> int:
    """Calculate the results for Part Two."""

    total = 0

    for sequence in sequences:
        total += sequence.prev

    return total
