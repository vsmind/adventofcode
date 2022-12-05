from re import match, sub


def read_input(input_file):
    """
    Find char position for containers in the input file

    :input_file: input file to read data from
    :return: a list containing each line in the file as a list item
    """
    file = open(input_file, 'r')
    return file.readlines()


def find_container_position(input_file):
    """
    Find char position for containers in the input file

    :input_file: input file to read data from
    :return: list with container stack position in input file
    """
    digits_position = []
    for line in input_file:
        if match("^ *[0-9][0-9 ]*$", line):
            for i, c in enumerate(line):
                if c.isdigit():
                    print(i)
                    digits_position.append(i)
            break
    return digits_position


def prepare_stacks(number_of_containers):
    """
    Prepare empty array of stacks

    :number_of_containers: input file to read data from
    :return: empty array for stack data
    """
    stack = []
    for _ in number_of_containers:
        stack.append([])
    return stack


def parse_input(input_file, stacks_position, stacks, orders):
    """
    Parse input to stacks and orders data

    :input_file: input file to read data from
    :stacks_position: position of the crates in the input
    :stacks: empty array for stacks data
    :orders: empty array for order data
    """
    read_orders = False
    for line in input_file:
        if len(line.strip()) == 0:
            read_orders = True

        if read_orders:
            order = parse_orders(line)
            if len(order) > 1:
                orders.append(order)
        else:
            crates_in_stacks(stacks_position, line, stacks)

    for st in stacks:
        st.reverse()


def crates_in_stacks(crates_position, line, stacks):
    """
    Parse crates in stacks and save it to the stacks list

    :crates_position: position of the crates in the input
    :line: stacks line from the input
    :stacks: empty array for stacks data
    """
    for i, position in enumerate(crates_position):
        if len(line) > position and line[position].isalpha():
            stacks[i].append(line[position])


def parse_orders(line):
    """
    Parse order from the input line

    :line: order line from the input
    :return: parsed order where 1 element is move, 2 element is from stack, 3 element is to stack
    """
    # Remove all chars that is not a number, remove space from the end of the string and split it by 2 spaces
    order_description = sub('[^0-9 _]', '', line).strip().split("  ")
    return order_description


def top_stacks(stacks):
    """
    Read the top crate form the stacks, and print the result

    :stacks: array with crates stack
    """
    top_stack = ""
    for stack in stacks:
        top_stack += stack[-1]
    print(top_stack)
