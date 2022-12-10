def parse_input(input_file):
    """
    Read input file and save data to the array

    :returns: two dimentional array with tree data
    """
    instructions = []
    input_file = open(input_file, 'r')
    instructions_file = input_file.readlines()
    for instruction in instructions_file:
        step = instruction.strip().split(" ")
        if len(step) == 1:
            instructions.append({"instruction": step[0]})
        else:
            instructions.append({"instruction": step[0], "value": step[1]})
    return instructions


def six_signal_strengths():
    register = {"cycle": 0, "x": 1, "crt": 0}
    signal_strength = []
    output_line = []
    instructions = parse_input("input")
    for i, instruction in enumerate(instructions):
        match instruction["instruction"]:
            case "addx":
                addx_instruction(register, instruction["value"], signal_strength, output_line)
            case "noop":
                noop_instruction(register, signal_strength, output_line)
    print(signal_strength)
    print("Sum of these six signal strengths", sum(signal_strength))


def addx_instruction(register, add, signal_strength, output_line):
    for x in range(0, 2):
        draw_pixel(register, output_line)
        register["cycle"] += 1
        check_cycle(register, signal_strength)
    register["x"] += int(add)


def noop_instruction(register, signal_strength, output_line):
    draw_pixel(register, output_line)
    register["cycle"] += 1
    check_cycle(register, signal_strength)


def draw_pixel(register, output_line):
    if register["crt"] in [register["x"] - 1, register["x"] , register["x"] + 1]:
        output_line.append("#")
    else:
        output_line.append(".")
    register["crt"] += 1

    if register["crt"] == 40:
        print("".join(output_line))
        output_line.clear()
        register["crt"] = 0


def check_cycle(register, signal_strength):
    if register["cycle"] in [20, 60, 100, 140, 180, 220]:
        signal_strength.append(register["x"] * register["cycle"])


if __name__ == "__main__":
    six_signal_strengths()
