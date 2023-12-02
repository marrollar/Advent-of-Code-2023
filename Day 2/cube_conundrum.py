import pprint
import math

constraint = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def cube_conundrum_1(games):
    valid_ids = []

    for game in games:
        game_id = game[0]
        draws = game[1]

        break_toggle = False

        for draw in draws:
            if break_toggle:
                break

            for color, limit in constraint.items():
                try:
                    if draw[color] > limit:
                        break_toggle = True
                        break
                except KeyError:
                    pass

        if not break_toggle:
            valid_ids.append(game_id)

    print(sum(valid_ids))


def cube_conundrum_2(games):
    powers = []

    for game in games:
        game_id = game[0]
        draws = game[1]

        min_required_cubes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        for draw in draws:
            for color, limit in draw.items():
                min_required_cubes[color] = max(min_required_cubes[color], limit)

        powers.append(min_required_cubes["red"] * min_required_cubes["green"] * min_required_cubes["blue"])

    print(sum(powers))


if __name__ == '__main__':
    inp_file = open("games", "r")

    games = []

    for line in inp_file.readlines():
        game_id = int(line.split(":")[0].split(" ")[1])
        draws = line.split(":")[1].split(";")

        draws_parsed = []

        for draw in draws:
            draw = draw.strip()
            cube_tokens = draw.split(",")

            cube_dict = {}

            for cubes in cube_tokens:
                cubes = cubes.strip()

                cube_counts = cubes.split(" ")

                cube_dict[cube_counts[1]] = int(cube_counts[0])

            draws_parsed.append(cube_dict)

        games.append((game_id, draws_parsed))

    cube_conundrum_1(games)
    cube_conundrum_2(games)
