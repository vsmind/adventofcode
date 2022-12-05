from tools import *


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


def rearrangement_procedure(stacks, orders):
    for order in orders:
        for i in range(int(order[0])):
            stacks[int(order[2]) - 1].append(stacks[int(order[1]) - 1].pop())


if __name__ == "__main__":
    top()