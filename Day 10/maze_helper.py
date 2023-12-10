compass_2_dir = {
    "north": (-1, 0),
    "south": (1, 0),
    "east": (0, 1),
    "west": (0, -1)
}

dir_2_compass = {
    (-1, 0): "north",
    (1, 0): "south",
    (0, 1): "east",
    (0, -1): "west"
}

invert_compass = {
    "north": "south",
    "south": "north",
    "east": "west",
    "west": "east"
}

translator = {
    "|": ["north", "south"],
    "-": ["east", "west"],
    "L": ["north", "east"],
    "J": ["north", "west"],
    "7": ["south", "west"],
    "F": ["south", "east"]
}

inv_translator = {
    "north": ["|", "7", "F"],
    "south": ["|", "L", "J"],
    "east": ["-", "J", "7"],
    "west": ['-', "L", "F"]
}


def get_adjacent(maze, coord):
    if coord[0] >= len(maze) or coord[1] >= len(maze[0]):
        raise IndexError("Gave out of bounds coordinate for maze")

    adj = {}

    for row, col in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        shifted_coords = (coord[0] + row, coord[1] + col)
        compass_dir = dir_2_compass[(row, col)]

        if shifted_coords[0] < 0 or shifted_coords[1] < 0:
            continue

        try:
            peek_node = maze[shifted_coords[0]][shifted_coords[1]]
        except IndexError:
            continue

        if peek_node != ".":
            adj[compass_dir] = peek_node

    return adj


def step(maze, cur_coord, direction):
    movement = compass_2_dir[direction]
    new_row = cur_coord[0] + movement[0]
    new_col = cur_coord[1] + movement[1]

    return (new_row, new_col), maze[new_row][new_col]
