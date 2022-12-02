result = {
    "A": {"X": 3, "Y": 6, "Z": 0},  # ROCK
    "B": {"X": 0, "Y": 3, "Z": 6},  # PAPER
    "C": {"X": 6, "Y": 0, "Z": 3}   # SCISSORS
        }


def calculate(openent, me):
    return shape_score(me) + result[openent][me]


def shape_score(shape):
    if shape == "X":  # Rock
        return 1
    elif shape == "Y":  # Paper
        return 2
    else:  # Scissors
        return 3


def main():
    file = open("input", 'r')
    strategy = file.readlines()
    total_score = 0
    for line in strategy:
        play = line.strip().split(" ")
        print(play)
        total_score += calculate(play[0], play[1])
    print(total_score)


if __name__ == "__main__":
    main()
