from multiprocessing import Process, Array
from math import lcm


def haunted_wasteland_1(directions, nodes):
    current_node = "AAA"
    dir_ind = 0
    steps = 0

    while True:
        try:
            current_node = nodes[current_node][directions[dir_ind]]
            dir_ind += 1
            steps += 1
        except IndexError:
            current_node = nodes[current_node][directions[0]]
            steps += 1
            dir_ind = 1

        if current_node == "ZZZ":
            print(steps)
            return steps


def threaded_search(start_node, directions, nodes, thread_idx, comm_array):
    def search():
        current_node = start_node
        dir_ind = 0
        steps = 0

        while True:
            try:
                current_node = nodes[current_node][directions[dir_ind]]
                dir_ind += 1
                steps += 1
            except IndexError:
                current_node = nodes[current_node][directions[0]]
                steps += 1
                dir_ind = 1

            if current_node[-1] == "Z":
                return steps

    comm_array[thread_idx] = search()


def haunted_wasteland_2(directions, nodes):
    start_nodes = [s for s in nodes.keys() if s[-1] == "A"]
    comm_array = Array("i", range(len(start_nodes)))

    pool = []

    for i in range(len(comm_array)):
        p = Process(target=threaded_search, args=(start_nodes[i], directions, nodes, i, comm_array))
        p.start()
        pool.append(p)

    for p in pool:
        p.join()

    print(comm_array[:], lcm(*comm_array))


if __name__ == '__main__':
    inp_file = open("map", "r")

    directions = inp_file.readline().strip()

    nodes = {}

    for line in inp_file.readlines():
        line = line.strip()

        if len(line) > 0:
            tokens = line.split("=")

            node = tokens[0].strip()

            tokens = tokens[1].replace("(", "").replace(")", "").split(",")

            nodes[node] = {
                "L": tokens[0].strip(),
                "R": tokens[1].strip()
            }

    haunted_wasteland_1(directions, nodes)
    haunted_wasteland_2(directions, nodes)
