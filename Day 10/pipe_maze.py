import pprint
from maze_helper import *
import shapely
import cv2
import numpy as np

pp = pprint.PrettyPrinter(indent=5)


def dfs(maze, cur_coord, from_compass, count):
    cur_node = maze[cur_coord[0]][cur_coord[1]]

    while True:
        if cur_coord == start_position:
            return count

        valid_compass = translator[cur_node]

        for compass_dir in valid_compass:
            if compass_dir != from_compass:
                from_compass = invert_compass[compass_dir]
                cur_coord, cur_node = step(maze, cur_coord, compass_dir)
                count += 1
                break


def pipe_maze_1(maze, cur_coord):
    adj_nodes = get_adjacent(maze, cur_coord)

    walk_compass = list(adj_nodes.keys())[0]
    from_compass = invert_compass[walk_compass]

    print(dfs(maze, step(maze, cur_coord, walk_compass)[0], from_compass, 1) / 2)


def dfs_trace(maze, cur_coord, from_compass):
    cur_node = maze[cur_coord[0]][cur_coord[1]]

    maze_mapped = []

    while True:
        maze_mapped.append(cur_coord)

        if cur_coord == start_position:
            return maze_mapped

        valid_compass = translator[cur_node]

        for compass_dir in valid_compass:
            if compass_dir != from_compass:
                from_compass = invert_compass[compass_dir]
                cur_coord, cur_node = step(maze, cur_coord, compass_dir)
                break


def pipe_maze_2(maze, cur_coord):
    adj_nodes = get_adjacent(maze, cur_coord)

    for dir, node in adj_nodes.items():
        if node in inv_translator[dir]:
            walk_compass = dir
            from_compass = invert_compass[walk_compass]
            break

    maze_coords = dfs_trace(maze, step(maze, cur_coord, walk_compass)[0], from_compass)

    scale = 5
    maze_img = np.zeros((len(maze) * scale, len(maze[0]) * scale, 3), np.uint8)

    for cur_coord, next_coord in zip(maze_coords, maze_coords[1:]):
        cv2.line(maze_img,
                 (cur_coord[0] * scale, cur_coord[1] * scale)[::-1],
                 (next_coord[0] * scale, next_coord[1] * scale)[::-1],
                 (0, 0, 255), 1, cv2.LINE_AA)

        # cv2.imshow("Maze", maze_img)
        # keyPressed = cv2.waitKey(0)
        # if keyPressed == ord("q"):
        #     break

    polygon = shapely.Polygon(maze_coords)
    pip_map = np.full((len(maze), len(maze[0])), False)
    dot_count = 0

    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == "." or (row, col) not in maze_coords:
                dot_count += 1
                pt = shapely.Point((row, col))
                pip = polygon.contains(pt)

                if pip:
                    pip_map[row][col] = True
                    cv2.circle(maze_img, (row * scale, col * scale)[::-1], scale // 2, (0, 255, 0), -1, cv2.LINE_AA)
                else:
                    cv2.circle(maze_img, (row * scale, col * scale)[::-1], scale // 2, (255, 0, 0), -1, cv2.LINE_AA)

    print(np.sum(pip_map), dot_count)

    cv2.imshow("Maze", maze_img)
    keyPressed = cv2.waitKey(0)
    if keyPressed == ord("q"):
        return


if __name__ == '__main__':
    inp_file = open("maze", "r")

    maze = []
    start_position = ()

    for row, line in enumerate(inp_file.readlines()):
        line = line.strip()
        maze.append([])

        for col, c in enumerate(line):
            maze[-1].append(c)

            if c == "S":
                start_position = (row, col)

    pipe_maze_1(maze, start_position)
    pipe_maze_2(maze, start_position)
