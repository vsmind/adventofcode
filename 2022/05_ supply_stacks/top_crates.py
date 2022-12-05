import re


def top():
    file = open("input", 'r')
    input = file.readlines()
    # Find position to containers
    stacks_position = find_container_position(input)
    # Create empty stacks and orders
    stacks = prepare_stacks(stacks_position)
    orders = []
    parse_input(input, stacks_position, stacks, orders)
    print("Stacks:", stacks)
    print("Orders:", orders)
    rearrangement_procedure(stacks, orders)
    print("Rearange:", stacks)
    top_stacks(stacks)


def find_container_position(input_file):
    digits_position = []
    for line in input_file:
        if re.match("^ *[0-9][0-9 ]*$", line):
            for i, c in enumerate(line):
                if c.isdigit():
                    print(i)
                    digits_position.append(i)
            break
    return digits_position


def prepare_stacks(number_of_containers):
    stack = []
    for i in number_of_containers:
        stack.append([])
    return stack


def parse_input(input_file, stacks_position, stacks, orders):
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
    for i, position in enumerate(crates_position):
        if len(line) > position and line[position].isalpha():
            stacks[i].append(line[position])


def parse_orders(line):
    order_description = re.sub('[^0-9 _]', '', line).strip().split("  ")
    # for position in line:
    #     if position.isdigit():
    #         order_description.append(position)
    print("Order:", order_description)
    return order_description


def rearrangement_procedure(stacks, orders):
    for order in orders:
        for i in range(int(order[0])):
            stacks[int(order[2]) - 1].append(stacks[int(order[1]) - 1].pop())


def top_stacks(stacks):
    top_stack = ""
    for stack in stacks:
        top_stack += stack[-1]
    print(top_stack)


if __name__ == "__main__":
    top()


# check string leng with container position
# add container to array