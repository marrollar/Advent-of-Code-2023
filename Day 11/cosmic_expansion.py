import pprint


def manhattan_distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])


# def create_universe_1(inp_file):
#     universe = []
#
#     for i, line in enumerate(inp_file.readlines()):
#         universe.append([c for c in line.strip()])
#         if "#" not in line:
#             universe.append(["."] * len(line))
#
#     universe = [list(l) for l in zip(*universe)]
#     i = len(universe) - 1
#     while i >= 0:
#         row = universe[i]
#         if "#" not in row:
#             universe.insert(i + 1, ["."] * len(row))
#         i -= 1
#
#     return universe
#
#
def create_universe_2(inp_file):
    universe = []
    expanded_rows = []
    expanded_cols = []

    for i, line in enumerate(inp_file.readlines()):
        universe.append([c for c in line.strip()])
        if "#" not in line:
            expanded_rows.append(i)

    universe = [list(l) for l in zip(*universe)]
    i = len(universe) - 1
    while i >= 0:
        row = universe[i]
        if "#" not in row:
            expanded_cols.append(i)
        i -= 1

    universe = [list(l) for l in zip(*universe)]
    return universe, expanded_rows, expanded_cols
#
#
def get_galaxy_coords(universe):
    galaxies = []

    for row in range(len(universe)):
        for col in range(len(universe[row])):
            if universe[row][col] == "#":
                galaxies.append((row, col))

    return galaxies
#
#
# def cosmic_expansion_1(galaxies):
#     gal_lens = 0
#
#     for i, gal1 in enumerate(galaxies):
#         for j, gal2 in enumerate(galaxies[i + 1:]):
#             gal_lens += manhattan_distance(gal1, gal2)
#
#     print(gal_lens)
#
#
def cosmic_expansion_2(galaxies, exp_rows, exp_cols, scaling_factor=1e6):
    gal_lens = 0

    for i, gal1 in enumerate(galaxies):
        for j, gal2 in enumerate(galaxies[i + 1:]):
            row_factor = 0
            col_factor = 0

            for row in exp_rows:
                if gal1[0] < row < gal2[0] or gal2[0] < row < gal1[0]:
                    row_factor += 1
            for col in exp_cols:
                if gal1[1] < col < gal2[1] or gal2[1] < col < gal1[1]:
                    col_factor += 1

            gal_lens += manhattan_distance(gal1, gal2) + (row_factor * scaling_factor) + (col_factor * scaling_factor)

    print(gal_lens)


if __name__ == '__main__':
    inp_file = open("universe", "r")
    universe_1 = create_universe_1(inp_file)
    galaxies_1 = get_galaxy_coords(universe_1)

    cosmic_expansion_1(galaxies_1)

    inp_file = open("universe", "r")
    universe_2, exp_rows, exp_cols = create_universe_2(inp_file)
    galaxies_2 = get_galaxy_coords(universe_2)

    cosmic_expansion_2(galaxies_2, exp_rows, exp_cols, scaling_factor=(1e6) - 1)
