def parse_input():
    """
    Read input file and save data to the array

    :returns: two dimentional array with tree data
    """
    bridge_path = []
    input_file = open("input_test", 'r')
    for path in input_file:
        step = path.strip().split(" ")
        bridge_path.append({step[0]: step[1]})
    return bridge_path


def find_visited_posotions():
    path = parse_input()
    print(path)


if __name__ == "__main__":
    find_visited_posotions()
