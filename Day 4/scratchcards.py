def scratchcards_1(deck):
    points = 0

    for _, have, winning_nums in deck:
        exponent = -1
        for num in have:
            if num in winning_nums:
                exponent += 1

        if exponent >= 0:
            points += 2 ** exponent

    print(points)


def scratchcards_2(deck):
    stack = [deck[-1]]
    memo = {len(deck): 0}
    total_scratchcards = 0

    def find_winners(have, winning_nums):
        won = 0
        for num in have:
            if num in winning_nums:
                won += 1

        return won

    deck_ind = 1

    while stack:
        scratchcard_ind, have, winning_nums = stack.pop()
        total_scratchcards += 1

        if len(stack) == 0 and deck_ind < len(deck):
            stack.append(deck[len(deck) - deck_ind - 1])
            deck_ind += 1

        try:
            total_scratchcards += memo[scratchcard_ind]
        except KeyError:
            copies_to_add = find_winners(have, winning_nums)

            memo[scratchcard_ind] = copies_to_add + sum(
                [memo[i]
                 for i in range(scratchcard_ind + 1, min(len(deck), scratchcard_ind + 1 + copies_to_add))
                 ])

            for hand in deck[scratchcard_ind + 1:scratchcard_ind + 1 + copies_to_add]:
                stack.append(hand)

    print(total_scratchcards)


if __name__ == '__main__':
    inp_file = open("cards", "r")

    cards = []

    for i, line in enumerate(inp_file.readlines()):
        tokens = line.split(":")[1].split('|')

        have = [int(num) for num in tokens[0].strip().split()]
        winning_nums = [int(num) for num in tokens[1].strip().split()]

        cards.append([i, have, winning_nums])

    scratchcards_1(cards)
    scratchcards_2(cards)
