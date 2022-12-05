from tools import *


def top():
    """
    Part one solution
    """
    task_input = read_input("input")
    # Find position to containers
    stacks_position = find_container_position(task_input)
    # Create empty stacks and orders
    stacks = prepare_stacks(stacks_position)
    orders = []
    # Read input and populate stacks and orders variables from the input
    parse_input(task_input, stacks_position, stacks, orders)
    # Rearange stacks according to the orders
    rearrangement_procedure(stacks, orders)
    # Find to of each stack
    top_stacks(stacks)


def rearrangement_procedure(stacks, orders):
    """
    Rearange stacks according to the orders

    :stacks: array with crates stack
    :stacks: array with orders
    """
    for order in orders:
        for i in range(int(order[0])):
            stacks[int(order[2]) - 1].append(stacks[int(order[1]) - 1].pop())


if __name__ == "__main__":
    top()
