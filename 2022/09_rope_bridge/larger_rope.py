from functools import reduce


def parse_input():
    """
    Read input file and saves data to the array

    :returns: list with motion commands
    """
    motions = []
    input_file = open("input", 'r')
    motions_list = input_file.readlines()
    for motion in motions_list:
        step = motion.strip().split(" ")
        motions.append({"direction": step[0], "value": step[1]})
    return motions


def follow_the_path(path):
    """
    Finding all positions where tail was

    :path: list with motion commands
    """
    knots = [{"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}]
    where_the_tail_was = []
    for step in path:
        move_direction(step, where_the_tail_was, knots)
    # All positions where was tail
    print("Tail was in: ", len(where_the_tail_was))
    # Find position visited at least once
    no_dub = reduce(lambda re, x: re+[x] if x not in re else re, where_the_tail_was, [])
    print("Tail was in unique: ", len(no_dub))


def move_direction(steps, where_the_tail_was, knots):
    """
    Move rope

    :steps: move the rope command
    :where_the_tail_was: list with positions for tails
    :knots: list with knots position
    """
    step = 0
    while step < int(steps["value"]):
        move_knot(steps, knots, where_the_tail_was)
        step += 1


def move_knot(steps, knots, where_the_tail_was):
    """
    Move knots

    :steps: move the rope command
    :where_the_tail_was: list with positions for tails
    :knots: list with knots position
    """
    for i, knot in enumerate(knots):
        # Move header
        if i == 0:
            move_head(steps, knot)
        else:
            if knots[i-1]["x"] != knot["x"] and knots[i-1]["y"] != knot["y"]:
                x_array = [knots[i-1]["x"], knot["x"]]
                x_change = max(x_array) - min(x_array)
                y_array = [knots[i-1]["y"], knot["y"]]
                y_change = max(y_array) - min(y_array)
                if x_change > 1 or y_change > 1:
                    move_diagonal(knots[i-1], knot)
            elif knots[i-1]["y"] != knot["y"]:  # move up/down
                y_array = [knots[i-1]["y"], knot["y"]]
                y_change = max(y_array) - min(y_array)
                if y_change > 1:
                    move_tail(knots[i-1], knot)
            elif knots[i-1]["x"] != knot["x"]:  # move left/right
                x_array = [knots[i-1]["x"], knot["x"]]
                x_change = max(x_array) - min(x_array)
                if x_change > 1:
                    move_tail(knots[i-1], knot)
        # Save position for tail
        if i == 9:
            where_the_tail_was.append({"x": knot["x"], "y": knot["y"]})


def move_head(steps, knot):
    """
    Move head accordin to command

    :steps: move the rope command
    :knot: head position
    """
    match steps["direction"]:
        case "U":
            knot["y"] += 1
        case "D":
            knot["y"] -= 1
        case "L":
            knot["x"] -= 1
        case "R":
            knot["x"] += 1


def move_tail(head, tail):
    """
    Move tain in x or y direction

    :head: head position
    :tail: tail position
    """
    if head["x"] == tail["x"] and head["y"] < tail["y"]:
        tail["y"] -= 1
    elif head["x"] == tail["x"] and head["y"] > tail["y"]:
        tail["y"] += 1
    elif head["y"] == tail["y"] and head["x"] < tail["x"]:
        tail["x"] -= 1
    elif head["y"] == tail["y"] and head["x"] > tail["x"]:
        tail["x"] += 1


def move_diagonal(head, tail):
    """
    Move tain in diagonal direction

    :head: head position
    :tail: tail position
    """
    if head["x"] > tail["x"] and head["y"] > tail["y"]:
        tail["x"] += 1
        tail["y"] += 1
    elif head["x"] < tail["x"] and head["y"] > tail["y"]:
        tail["x"] -= 1
        tail["y"] += 1
    elif head["x"] < tail["x"] and head["y"] < tail["y"]:
        tail["x"] -= 1
        tail["y"] -= 1
    elif head["x"] > tail["x"] and head["y"] < tail["y"]:
        tail["x"] += 1
        tail["y"] -= 1


def find_visited_posotions():
    """
    Run script to find visited position
    """
    path = parse_input()
    follow_the_path(path)


if __name__ == "__main__":
    find_visited_posotions()
