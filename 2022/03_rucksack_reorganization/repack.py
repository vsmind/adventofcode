item_priority = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    file = open("input", 'r')
    strategy = file.readlines()
    # Code result
    sum_of_priorities = 0
    for line in strategy:
        bag = line.strip()
        # Find items in first and second compartments
        first_compartment = bag[0:len(bag)//2]
        second_compartment = bag[len(bag)//2:]
        # Add items to set collection
        com_set = set(first_compartment)
        com2_set = set(second_compartment)
        # Find the same item both compartments
        item = com_set.intersection(com2_set)
        # Calculate priority for items
        sum_of_priorities += item_priority.find(item.pop())
    # Print result
    print("Sum of the priorities", sum_of_priorities)


if __name__ == "__main__":
    main()
