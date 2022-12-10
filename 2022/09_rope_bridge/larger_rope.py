from functools import reduce


def parse_input():
    """
    Read input file and save data to the array

    :returns: two dimentional array with tree data
    """
    bridge_path = []
    input_file = open("input", 'r')
    head_path = input_file.readlines()
    for path in head_path:
        step = path.strip().split(" ")
        bridge_path.append({"direction": step[0], "value": step[1]})
    return bridge_path


def follow_the_path(path):
    knots = [{"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}]
    where_the_tail_was = []
    for step in path:
        move_direction(step, where_the_tail_was, knots)
    # print("was",where_the_tail_was)
    no_dub = reduce(lambda re, x: re+[x] if x not in re else re, where_the_tail_was, [])
    print(len(no_dub))


def move_direction(steps, where_the_tail_was, knots):
    step = 0
    while step < int(steps["value"]):
        move_knot(steps, knots, where_the_tail_was)
        step += 1

def move_knot(steps, knots, where_the_tail_was):
    #print(knots)
    for i, knot in enumerate(knots):
        if i == 0:
            move(steps, knot)
            #print("HEAD", i, knot)
        else:
            #print("Tail")  # move diagonal
            if knots[i-1]["x"] != knot["x"] and knots[i-1]["y"] != knot["y"]:
                x_array = [knots[i-1]["x"], knot["x"]]
                x_change = max(x_array) - min(x_array)
                y_array = [knots[i-1]["y"], knot["y"]]
                y_change = max(y_array) - min(y_array)
                if x_change > 1 or y_change > 1:
                    move_diagonal(steps, knots[i-1], knot)
            if knots[i-1]["y"] != knot["y"]:  # move up/down
                y_array = [knots[i-1]["y"], knot["y"]]
                y_change = max(y_array) - min(y_array)
                if y_change > 1:
                    move(steps, knot)
            if knots[i-1]["x"] != knot["x"]:  # move left/right
                x_array = [knots[i-1]["x"], knot["x"]]
                x_change = max(x_array) - min(x_array)
                if x_change > 1:
                    move(steps, knot)
            #print("KNOT", i, knot)

        if i == 9:
            # print("knt",knot)
            where_the_tail_was.append({"x": knot["x"], "y": knot["y"]})



def move(steps, knot):
    match steps["direction"]:
        case "U":
            knot["y"] += 1
        case "D":
            knot["y"] -= 1
        case "L":
            knot["x"] -= 1
        case "R":
            knot["x"] += 1


def move_diagonal(steps, head, tail):
    match steps["direction"]:
        case "U":
            if head["x"] > tail["x"]:
                tail["x"] += 1
                tail["y"] += 1
            else:
                tail["x"] -= 1
                tail["y"] += 1
        case "D":
            if head["x"] > tail["x"]:
                tail["x"] += 1
                tail["y"] -= 1
            else:
                tail["x"] -= 1
                tail["y"] -= 1
        case "L":
            if head["y"] > tail["y"]:
                tail["x"] -= 1
                tail["y"] += 1
            else:
                tail["x"] -= 1
                tail["y"] -= 1
        case "R":
            if head["y"] > tail["y"]:
                tail["x"] += 1
                tail["y"] += 1
            else:
                tail["x"] += 1
                tail["y"] -= 1


    #match steps["direction"]:
    #    case "U":
    #        position["y"] += 1
    #        #print("top")
    #    case "D":
    #        position["y"] -= 1
    #        #print("down")
    #    case "L":
    #        position["x"] -= 1
    #        #print("Left")
    #    case "R":
    #        position["x"] += 1
    #       #print("Right")
    #        check_tail(position, head_previous_position, tail_position)
    #where_the_tail_was.append({"x": tail_position["x"], "y": tail_position["y"]})
    #if tail_position not in where_the_tail_was:
    #    where_the_tail_was.append({"x": tail_position["x"], "y": tail_position["y"]})
    #print("Tail was", where_the_tail_was)
    #print("________________________")

def find_visited_posotions():
    path = parse_input()
    follow_the_path(path)


if __name__ == "__main__":
    find_visited_posotions() #6831 too high