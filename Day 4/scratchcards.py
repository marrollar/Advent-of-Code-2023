def scratchcards_1(deck):
    points = 0

    for _, have, winning_nums in deck:
        exponent = -1 + sum(1 for num in have if num in winning_nums)

        if exponent >= 0:
            points += 2 ** exponent

    print(points)


def scratchcards_2(deck):
    stack = [deck[-1]]
    memo = {len(deck): 0}
    total_scratchcards = 0

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
            copies_to_add = sum(1 for num in have if num in winning_nums)
            memo[scratchcard_ind] = copies_to_add

            for i in range(scratchcard_ind + 1, min(len(deck), scratchcard_ind + 1 + copies_to_add)):
                memo[scratchcard_ind] += memo[i]
                stack.append(deck[i])

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
