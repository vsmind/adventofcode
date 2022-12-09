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
        #print(step)
        move_directoin(step, starting_position, where_the_tail_was, tail_position)
    #no_dub = [dict(t) for t in {tuple(d.items()) for d in where_the_tail_was}]
    no_dub = reduce(lambda re, x: re+[x] if x not in re else re, where_the_tail_was, [])
    #for i in where_the_tail_was:
    #    print(i)
    #print("_____")


    #for b in no_dub:
    #    print(b)
    print(len(no_dub))

def move_directoin(steps, position, where_the_tail_was, tail_position):
    step = 0
    head_previous_position = {"x": 0, "y": 0}
    while step < int(steps["value"]):
        #print(steps["direction"], steps["value"], step)
        update_head_previous_position(head_previous_position, position["x"], position["y"])
        match steps["direction"]:
            case "U":
                position["y"] += 1
                #print("top")
            case "D":
                position["y"] -= 1
                #print("down")
            case "L":
                position["x"] -= 1
                #print("Left")
            case "R":
                position["x"] += 1
                #print("Right")
        check_tail(position, head_previous_position, tail_position)
        where_the_tail_was.append({"x": tail_position["x"], "y": tail_position["y"]})
        #if tail_position not in where_the_tail_was:
        #    where_the_tail_was.append({"x": tail_position["x"], "y": tail_position["y"]})
        #print("Tail was", where_the_tail_was)
        #print("________________________")
        step += 1


def update_head_previous_position(head_previous_position, x, y):
    head_previous_position["x"] = x
    head_previous_position["y"] = y


def check_tail(head_position, head_previous_position, tail_position):
    #print("Head", head_position)
    #print("Head prev", head_previous_position)
    #print("Tail position", tail_position)
    #print()
    #print("Y max", max([abs(head_position["y"]), abs(tail_position["y"])]) - min([abs(head_position["y"]), abs(tail_position["y"])]))
    x_array = [head_position["x"], tail_position["x"]]
    x_change = max(x_array) - min(x_array)
    y_array = [head_position["y"], tail_position["y"]]
    y_change = max(y_array) - min(y_array)
    if x_change > 1 or y_change > 1:
        tail_position["x"] = head_previous_position["x"]
        tail_position["y"] = head_previous_position["y"]
    #print("UPDATED TAIL", tail_position)


if __name__ == "__main__":
    find_visited_posotions()
