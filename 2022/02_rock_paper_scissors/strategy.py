result_point = {
    "X": 0,  # LOSE
    "Y": 3,  # DRAW
    "Z": 6  # WIN
}

results = {
    "A": {0: "C", 3: "A", 6: "B"},  # ROCK
    "B": {0: "A", 3: "B", 6: "C"},  # PAPER
    "C": {0: "B", 3: "C", 6: "A"},  # SCISSORS
}

shape_result = {
    "A": 1,
    "B": 2,
    "C": 3,
}


def calculate_two(openent, me):
    round_result = result_point[me]
    play_result = shape_result[results[openent][round_result]]
    print(play_result, "+", round_result)
    return round_result + play_result


def main():
    file = open("input", 'r')
    strategy = file.readlines()
    total_score = 0
    for line in strategy:
        play = line.strip().split(" ")
        print(play)
        total_score += calculate_two(play[0], play[1])
    print(total_score)


if __name__ == "__main__":
    main()
