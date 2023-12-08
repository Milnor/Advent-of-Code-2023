#!/usr/bin/env python3
""" Functions to solve the Day Seven challenges. """

TITLE = "Camel Cards"

hand_types = {
    "high": 0,  # high card
    "one": 1,   # one pair
    "two": 2,   # two pair
    "three": 3, # three of a kind
    "full": 4,  # full house
    "four": 5,  # four of a kind
    "five": 6,  # five of a kind
}

card_strengths = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}

card_strengths2 = {
    'J': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'Q': 11,
    'K': 12,
    'A': 13,
}

class Hand:
    """Hand of cards and its bid."""

    def __init__(self, cards: str, bid: str, part_two: bool=False):
        self.cards = cards
        self.bid = int(bid)
        self.part_two = part_two    # flag to trigger alternate rules for Part Two
        self.card_counts = self.get_counts()
        self.hand_type = self.get_type()
    
    def __str__(self):
        return f"Hand: cards={self.cards}, bid={self.bid}, type={self.hand_type}"

    def get_counts(self) -> dict:
        """Populate dictionary of card counts"""
        counts = {
            'A': 0,
            'K': 0,
            'Q': 0,
            'J': 0,
            'T': 0,
            '9': 0,
            '8': 0,
            '7': 0,
            '6': 0,
            '5': 0,
            '4': 0,
            '3': 0,
            '2': 0,
        }
        for card in self.cards:
            counts[card] += 1
        return counts

    def get_type(self) -> str:
        """Determine type of hand"""
        #highest = 0
        #second_highest = 0
        # for count in self.card_counts:
        #     if self.card_counts[count] > highest:
        #         highest = self.card_counts[count]
        #     elif self.card_counts[count] > second_highest:
        #         second_highest = self.card_counts[count]
        if self.part_two:
            jokers = self.card_counts['J']
            counts = counts = [self.card_counts[i] for i in self.card_counts.keys() if i != 'J']
            sorted_counts = sorted(counts)
            highest = sorted_counts[-1] + jokers
            second_highest = sorted_counts[-2]
        else:
            counts = [self.card_counts[i] for i in self.card_counts.keys()] 
            sorted_counts = sorted(counts)
            highest = sorted_counts[-1]
            second_highest = sorted_counts[-2]
            
        if highest == 5 and second_highest == 0:
            return "five"
        elif highest == 4 and second_highest == 1:
            return "four"
        elif highest == 3 and second_highest == 2:
            return "full"
        elif highest == 3 and second_highest == 1:
            return "three"
        elif highest == 2 and second_highest == 2:
            return "two"
        elif highest == 2 and second_highest == 1:
            return "one"
        elif highest == 1 and second_highest == 1:
            return "high"
        else:
            raise ValueError(f"{highest=}, {second_highest=}")

def weaker_hand(first: Hand, second: Hand, part_two: bool) -> bool:
    """True if first is the weaker hand, False otherwise."""

    # New special handling to distinguish Parts One and Two
    if part_two:
        strengths = card_strengths2
    else:
        strengths = card_strengths

    for i in range(len(first.cards)):
        first_card = first.cards[i]
        second_card = second.cards[i]
        #print(f"{i}: {first.cards} vs {second.cards} --> {first_card} v {second_card}")
        if strengths[first_card] < strengths[second_card]:
            #print("\tTrue")
            return True
        elif strengths[first_card] > strengths[second_card]:
            #print("\tFalse")
            return False
        else:
            # Tie, keep looking
            #print("\tTie")
            continue

def insert_in_order(hand_list: list[Hand], new_hand: Hand, part_two: bool=False):
    """Insert hand in list, maintaing low-to-high ordering."""
    
    if not hand_list:
        hand_list.append(new_hand)
    else:
        location = -1
        for i, entry in enumerate(hand_list):
            if weaker_hand(new_hand, entry, part_two):
                location = i
                break

        # In case new_hand was strongest
        if location < 0:
            location = len(hand_list)

        # should work even if initial list was empty
        hand_list.insert(location, new_hand)


def part_one(data: list[str]) -> int:
    """Calculate the results for Part One."""

    total = 0
    # group by hand type first so we *never* have to sort everything
    all_highs = []  # high card hands
    all_ones = []   # one pair hands
    all_twos = []   # two pair hands
    all_threes = [] # three of a kind hands
    all_fulls = []  # full house hands
    all_fours = []  # four of a kind hands
    all_fives = []  # five of a kind hands
    all_hands = [
        all_highs,
        all_ones,
        all_twos,
        all_threes,
        all_fulls,
        all_fours,
        all_fives,
    ]
    
    for line in data:
        cards, bid = line.split()
        new_hand = Hand(cards, bid)
        if new_hand.hand_type == "five":
            insert_in_order(all_fives, new_hand)
        elif new_hand.hand_type == "four":
            insert_in_order(all_fours, new_hand)
        elif new_hand.hand_type == "full":
            insert_in_order(all_fulls, new_hand)
        elif new_hand.hand_type == "three":
            insert_in_order(all_threes, new_hand)
        elif new_hand.hand_type == "two":
            insert_in_order(all_twos, new_hand)
        elif new_hand.hand_type == "one":
            insert_in_order(all_ones, new_hand)
        elif new_hand.hand_type == "high":
            insert_in_order(all_highs, new_hand)
        else:
            raise ValueError(f"Bad hand type: {new_hand.hand_type}")

    rank = 1
    for hand_type in all_hands:
        for hand in hand_type:
            #print(hand)
            total += rank * hand.bid
            #print(f"{rank} * {hand.bid} = {rank * hand.bid}\tTOTAL: {total}")
            rank += 1

    return total


def part_two(data: list[str]) -> int:
    """Calculate the results for Part Two."""

    # Like previous, except 'J' is now the Joker wildcard that
    # strengthens the type of hand, but with a lower individual card value.

    all_highs = []  # high card hands
    all_ones = []   # one pair hands
    all_twos = []   # two pair hands
    all_threes = [] # three of a kind hands
    all_fulls = []  # full house hands
    all_fours = []  # four of a kind hands
    all_fives = []  # five of a kind hands
    all_hands = [
        all_highs,
        all_ones,
        all_twos,
        all_threes,
        all_fulls,
        all_fours,
        all_fives,
    ]
    
    for line in data:
        cards, bid = line.split()
        new_hand = Hand(cards, bid, part_two=True)
        if new_hand.hand_type == "five":
            insert_in_order(all_fives, new_hand, part_two=True)
        elif new_hand.hand_type == "four":
            insert_in_order(all_fours, new_hand, part_two=True)
        elif new_hand.hand_type == "full":
            insert_in_order(all_fulls, new_hand, part_two=True)
        elif new_hand.hand_type == "three":
            insert_in_order(all_threes, new_hand, part_two=True)
        elif new_hand.hand_type == "two":
            insert_in_order(all_twos, new_hand, part_two=True)
        elif new_hand.hand_type == "one":
            insert_in_order(all_ones, new_hand, part_two=True)
        elif new_hand.hand_type == "high":
            insert_in_order(all_highs, new_hand, part_two=True)
        else:
            raise ValueError(f"Bad hand type: {new_hand.hand_type}")

    total = 0
    rank = 1
    for hand_type in all_hands:
        for hand in hand_type:
            print(hand)
            total += rank * hand.bid
            print(f"{rank} * {hand.bid} = {rank * hand.bid}\tTOTAL: {total}")
            rank += 1

    return total
