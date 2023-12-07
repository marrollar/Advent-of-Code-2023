from poker_helper import *
from time import perf_counter


def camel_cards_1(hands):
    converted_hands = []

    for cards, bid in hands:
        converted_hands.append(Hand(cards, bid))

    final_score = 0
    for i, camel_hand in enumerate(sorted(converted_hands)):
        final_score += (i + 1) * camel_hand.bid

    print(final_score)


def camel_cards_2(hands):
    converted_hands = []

    for cards, bid in hands:
        converted_hands.append(HandJoker(cards, bid))

    final_score = 0
    for i, camel_hand in enumerate(sorted(converted_hands)):
        final_score += (i + 1) * camel_hand.bid

    print(final_score)


if __name__ == '__main__':
    inp_file = open("cards", "r")

    hands = []

    for line in inp_file.readlines():
        tokens = line.strip().split()
        hands.append((tokens[0], int(tokens[1])))

    start = perf_counter()
    camel_cards_1(hands)
    print(perf_counter() - start)
    start = perf_counter()
    camel_cards_2(hands)
    print(perf_counter() - start)
