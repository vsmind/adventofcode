def parse_input(input_file):
    heightmap = []
    input_file = open(input_file, 'r')
    for path in input_file:
        heightmap.append(path.strip())
    return heightmap


def move_direction(heightmap, starting_position, steps):
    if starting_position["y"] + 1 > 0:
        if can_move(heightmap, starting_position)
        print("Move up")

    if starting_position["y"] + 1 < len(heightmap):
        print("Move down")

    if starting_position["x"] + 1 < len(heightmap):
        print("Move left")

    if starting_position["x"] + 1 < len(heightmap):
        print("Move right")


def can_move(heightmap, starting_position, new_position):
    starting_position_height = ord(heightmap[starting_position["x"]][starting_position["x"]])
    new_position_height = ord(heightmap[new_position["x"]][new_position["x"]])
    if new_position_height - starting_position_height <= 1:
        return True
    else:
        return False



def move(heightmap, starting_position):
    steps = 0
    print(heightmap[starting_position["x"]][starting_position["y"]])

    # Check X in bounds
    if heightmap[starting_position["x"]] < 0 or heightmap[starting_position["x"]] > len(heightmap):
        print("out of bounds")

    # Check Y in bounds

    # UP





def climbing():
    print("Climbing")
    starting_position = {"x": 0, "y": 0}
    heightmap = parse_input("input_test")
    print(heightmap)
    move(heightmap, starting_position)


if __name__ == "__main__":
    climbing()
