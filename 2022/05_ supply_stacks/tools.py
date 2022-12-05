from re import match, sub

def find_container_position(input_file):
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
    order_description = sub('[^0-9 _]', '', line).strip().split("  ")
    print("Order:", order_description)
    return order_description


def top_stacks(stacks):
    top_stack = ""
    for stack in stacks:
        top_stack += stack[-1]
    print(top_stack)