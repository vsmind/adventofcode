import sys


def parse_input(input_file):
    heightmap = []
    input_file = open(input_file, 'r')
    for path in input_file.readlines():
        heightmap.append(path.strip())
    return heightmap


def move_direction(heightmap, starting_position, steps, way_to_the_top, routes):

    #print("____________________")
    #print("Way ", way_to_the_top)

    #if heightmap[starting_position["x"]][starting_position["y"]] == 'p':
    #    print("FOT DEBUG")

    if heightmap[starting_position["x"]][starting_position["y"]] == 'E':
        print("AT THE TOP", len(way_to_the_top) - 1)
        print(way_to_the_top)
        #print("Way:", len(way_to_the_top) - 1)
        routes.append(len(way_to_the_top) - 1)
        print(min(routes))
        print("____________")

    if starting_position["x"] + 1 < len(heightmap):  # Up
        new_position = {"x": starting_position["x"] + 1, "y": starting_position["y"]}
        if can_move(heightmap, starting_position, new_position) and dont_move_back(new_position, way_to_the_top):
            w = [*way_to_the_top, starting_position]
            steps += 1
            move_direction(heightmap, new_position, steps, w, routes)

    if starting_position["x"] - 1 > -1:  # Down
        new_position = {"x": starting_position["x"] - 1, "y": starting_position["y"]}
        if can_move(heightmap, starting_position, new_position) and dont_move_back(new_position, way_to_the_top):
            w = [*way_to_the_top, starting_position]
            steps += 1
            move_direction(heightmap, new_position, steps, w, routes)

    if starting_position["y"] + 1 < len(heightmap[0]):
        new_position = {"x": starting_position["x"], "y": starting_position["y"] + 1}
        if can_move(heightmap, starting_position, new_position) and dont_move_back(new_position, way_to_the_top):
            w = [*way_to_the_top, starting_position]
            steps += 1
            move_direction(heightmap, new_position, steps, w, routes)

    if starting_position["y"] - 1 > -1:
        new_position = {"x": starting_position["x"], "y": starting_position["y"] - 1}
        if can_move(heightmap, starting_position, new_position) and dont_move_back(new_position, way_to_the_top):
            w = [*way_to_the_top, starting_position]
            steps += 1
            move_direction(heightmap, new_position, steps, w, routes)

    #print(way_to_the_top)
    #del way_to_the_top[:]
    # print("Dead end")

def dont_move_back(position, prev_position):
    if position in prev_position:
        return False
    else:
        return True


def can_move(heightmap, starting_position, new_position):
    #print(heightmap)
    #print("STR", starting_position, heightmap[starting_position["x"]][starting_position["y"]])
    #print("NEW", new_position, heightmap[new_position["x"]][new_position["y"]])
    starting_position_height = heightmap[starting_position["x"]][starting_position["y"]] == 'S' and ord('a') or ord(heightmap[starting_position["x"]][starting_position["y"]])
    new_position_height = heightmap[new_position["x"]][new_position["y"]] == 'E' and ord('z') or ord(heightmap[new_position["x"]][new_position["y"]])
    if starting_position_height - new_position_height >= -1: # 10 - 12 = -2
        return True
    else:
        return False



def move(heightmap, starting_position):
    steps = 0
    way_to_the_top = [{"x": 0, "y": 0}]
    routes = []
    #print(heightmap[starting_position["x"]][starting_position["y"]])
    way = move_direction(heightmap, starting_position, steps, way_to_the_top, routes)


def climbing():
    print("Climbing")
    starting_position = {"x": 0, "y": 0}  # {"x": 20, "y": 0}
    heightmap = parse_input("input_test")
    print("Start", heightmap[starting_position["x"]][starting_position["y"]])
    print_path(heightmap)
    move(heightmap, starting_position)


def print_path(heightmap):
    for line in heightmap:
        print(line)


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    climbing()
