from collections import OrderedDict, Counter
from functools import reduce


def parse_input():
    """
    Read input file and save data to the array

    :returns: two dimentional array with tree data
    """
    bridge_path = []
    input_file = open("input", 'r')
    for path in input_file:
        step = path.strip().split(" ")
        bridge_path.append({"direction": step[0], "value": step[1]})
    return bridge_path


def find_visited_posotions():
    path = parse_input()
    follow_the_path(path)


def follow_the_path(path):
    starting_position = {"x": 0, "y": 0}
    tail_position = {"x": 0, "y": 0}
    where_the_tail_was = []
    for step in path:
        move_direction(step, starting_position, where_the_tail_was, tail_position)
    no_dub = reduce(lambda re, x: re+[x] if x not in re else re, where_the_tail_was, [])
    print(len(no_dub))


def move_direction(steps, position, where_the_tail_was, tail_position):
    """
    Move rope position

    :steps: previous position for head
    :position: x position
    :where_the_tail_was: y position
    :tail_position:
    """
    step = 0
    head_previous_position = {"x": 0, "y": 0}
    while step < int(steps["value"]):
        update_head_previous_position(head_previous_position, position["x"], position["y"])
        match steps["direction"]:
            case "U":
                position["y"] += 1
            case "D":
                position["y"] -= 1
            case "L":
                position["x"] -= 1
            case "R":
                position["x"] += 1
        check_tail(position, head_previous_position, tail_position)
        where_the_tail_was.append({"x": tail_position["x"], "y": tail_position["y"]})
        step += 1


def update_head_previous_position(head_previous_position, x, y):
    """
    Update previous head position

    :head_previous_position: previous position for head
    :x: x position
    :y: y position
    """
    head_previous_position["x"] = x
    head_previous_position["y"] = y


def check_tail(head_position, head_previous_position, tail_position):
    """
    Check if tail should be moved and move it to the previous head position

    :head_position: head position
    :head_previous_position: previous position for head
    :tail_position: tail position
    """
    x_array = [head_position["x"], tail_position["x"]]
    x_change = max(x_array) - min(x_array)
    y_array = [head_position["y"], tail_position["y"]]
    y_change = max(y_array) - min(y_array)
    if x_change > 1 or y_change > 1:
        tail_position["x"] = head_previous_position["x"]
        tail_position["y"] = head_previous_position["y"]


if __name__ == "__main__":
    find_visited_posotions()
