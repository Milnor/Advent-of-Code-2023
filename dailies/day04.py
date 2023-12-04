#!/usr/bin/env python3
""" Functions to solve the Day Four challenges. """

from dataclasses import dataclass

TITLE = "Scratchcards"


@dataclass
class Card:
    """Simple model of a scratchcard."""

    wins: int  # how many times it won
    copies: int  # copies of the card


def count_wins(data: str) -> int:
    """Count how many numbers in card are winners."""

    # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    _, all_numbers = data.split(":")
    my_numbers, winning_numbers = all_numbers.split("|")
    my_numbers = my_numbers.split()
    winning_numbers = winning_numbers.split()
    wins = 0
    for each in my_numbers:
        if each in winning_numbers:
            wins += 1
    return wins


def create_card(data: str) -> Card:
    """Create a Card object from a string of card data."""

    wins = count_wins(data)
    return Card(wins=wins, copies=1)


def calculate_points(card: str) -> int:
    """Calculate points won by card."""

    wins = count_wins(card)

    if wins > 0:
        wins = 2 ** (wins - 1)

    return wins


def part_one(data: list[str]) -> int:
    """Calculate the results for Part One."""

    total = 0

    for line in data:
        total += calculate_points(line.strip())

    return total


def part_two(data: list[str]) -> int:
    """Calculate the results for Part Two."""

    total = 0
    scratchcards = {}

    # Build the original stack of cards
    for i, line in enumerate(data, 1):
        scratchcards[i] = create_card(line.strip())

    # Award copies for wins
    for i, card in scratchcards.items():
        for _ in range(card.copies):
            for win in range(1, card.wins + 1):
                if i + win <= len(scratchcards):
                    scratchcards[i + win].copies += 1

    for i, card in scratchcards.items():
        total += card.copies

    return total
