from functools import total_ordering
from collections import Counter


def determine_hand_type(cards):
    cards_count = Counter(cards)

    if 5 in cards_count.values():
        return "5"
    elif 4 in cards_count.values():
        return "4"
    elif 3 in cards_count.values() and 2 in cards_count.values():
        return "house"
    elif 3 in cards_count.values():
        return "3"
    elif 2 in cards_count.values():
        if Counter(cards_count.values())[2] == 2:
            return "2p"
        else:
            return "1p"
    else:
        return "high"


def determine_hand_type_joker(cards):
    if "J" not in cards:
        return determine_hand_type(cards)
    else:
        cards_count = Counter(cards)
        if cards_count["J"] == 5:
            return "5"
        elif cards_count["J"] == 4:
            return "5"

        elif cards_count["J"] == 3:
            if 2 in cards_count.values():
                # JJJ 22
                return "5"
            else:
                # JJJ 23
                return "4"

        elif cards_count["J"] == 2:
            if 3 in cards_count.values():
                # JJ 222
                return "5"
            else:
                tmp_cnter = Counter(cards_count.values())

                if tmp_cnter[2] == 2:
                    # JJ 22 3
                    return "4"
                else:
                    # JJ 123
                    return "3"

        else:
            if 4 in cards_count.values():
                # J 2222
                return "5"
            elif 3 in cards_count.values():
                # J 222 3
                return "4"
            else:
                tmp_cnter = Counter(cards_count.values())

                if tmp_cnter[2] == 2:
                    # J 22 33
                    return "house"
                elif tmp_cnter[2] == 1:
                    # J 22 34
                    return "3"
                else:
                    # J 2345
                    return "1p"


@total_ordering
class HandType:

    def __init__(self, string_rep):
        self.type = string_rep
        if string_rep == "5":
            self.order = 7
        elif string_rep == "4":
            self.order = 6
        elif string_rep == "house":
            self.order = 5
        elif string_rep == "3":
            self.order = 4
        elif string_rep == "2p":
            self.order = 3
        elif string_rep == "1p":
            self.order = 2
        elif string_rep == "high":
            self.order = 1

    def __lt__(self, other):
        return self.order < other.order

    def __eq__(self, other):
        return self.order == other.order

    def __repr__(self):
        return self.type


class Card:

    def __init__(self, card_str):
        self.card_str = card_str

        if card_str.isnumeric():
            self.order = int(card_str)
        elif card_str == "T":
            self.order = 10
        elif card_str == "J":
            self.order = 11
        elif card_str == "Q":
            self.order = 12
        elif card_str == "K":
            self.order = 13
        elif card_str == "A":
            self.order = 14

    def __lt__(self, other):
        return self.order < other.order

    def __eq__(self, other):
        return self.order == other.order


@total_ordering
class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.type = HandType(determine_hand_type(cards))

    def __lt__(self, other):
        if self.type < other.type:
            return True
        elif self.type == other.type:
            for c1, c2 in zip(self.cards, other.cards):
                if Card(c1) < Card(c2):
                    return True
                elif Card(c1) > Card(c2):
                    return False

        return False

    def __eq__(self, other):
        if self.type == other.type:
            for c1, c2 in zip(self.cards, other.cards):
                if Card(c1) != Card(c2):
                    return False
        return True

    def __repr__(self):
        return f"({self.cards}, {self.type}, {self.bid})"


class CardJoker(Card):
    def __init__(self, card_str):
        super().__init__(card_str)
        if card_str == "J":
            self.order = 1


class HandJoker(Hand):

    def __init__(self, cards, bid):
        super().__init__(cards, bid)
        self.type = HandType(determine_hand_type_joker(cards))

    def __lt__(self, other):
        if self.type < other.type:
            return True
        elif self.type == other.type:
            for c1, c2 in zip(self.cards, other.cards):
                if CardJoker(c1) < CardJoker(c2):
                    return True
                elif CardJoker(c1) > CardJoker(c2):
                    return False

        return False

    def __eq__(self, other):
        if self.type == other.type:
            for c1, c2 in zip(self.cards, other.cards):
                if CardJoker(c1) != CardJoker(c2):
                    return False
        return True
