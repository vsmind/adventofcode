import math


def parse_input(day_input):
    """
    Read input file and saves data to the array

    :day_input: name of the input file
    :returns: list with monkey dictionary
    """
    monkeys = []
    input_file = open(day_input, 'r')
    monkeys_observations = input_file.readlines()

    for observation in monkeys_observations:
        if observation.startswith('Monkey'):
            monkeys.append({})
            monkeys[-1]["number"] = int(''.join([n for n in observation if n.isdigit()]))

        if observation.strip().startswith('Starting items'):
            items = [int(item_number) for item_number in observation.strip().removeprefix('Starting items: ').split(', ')]
            monkeys[-1]["items"] = items

        if observation.strip().startswith('Operation'):
            monkeys[-1]["operation"] = observation.strip().removeprefix('Operation: new = ')

        if observation.strip().startswith('Test'):
            monkeys[-1]["test"] = int(''.join([n for n in observation if n.isdigit()]))

        if observation.strip().startswith('If true'):
            monkeys[-1]["true"] = int(''.join([n for n in observation if n.isdigit()]))

        if observation.strip().startswith('If false'):
            monkeys[-1]["false"] = int(''.join([n for n in observation if n.isdigit()]))

    return monkeys


def add_number_of_inspected_items(monkeys):
    """
    Add inspected parameter to the dictionary

    :monkeys: list with monkeys dictionary
    """
    for monkey in monkeys:
        monkey["inspected"] = 0


def calculate_worry_level(item, operation):
    """
    Add inspected parameter to the dictionary

    :item: starting worry level for item
    :operation: type of worry level operation
    :item: new value of worry level for item
    """
    parse_operation = operation.split(" ")
    match parse_operation[1]:
        case("*"):
            if parse_operation[2].isnumeric():
                item = item * int(parse_operation[2])
            else:
                item = item * item
        case("+"):
            if parse_operation[2].isnumeric():
                item = item + int(parse_operation[2])
            else:
                item = item + item
        case(_):
            print("ERROR")
    return item


def bored_monkey(worry_level):
    """
    Calculate worry level for an item after a monkey getting bored

    :worry_level: worry level for an item
    :return: new value of worry level after monkey get bored
    """
    return math.floor(worry_level / 3)


def throws_an_item(worry_level, monkey, monkeys):
    """
    Calculate where a monkey trows an item

    :worry_level: worry level for an item
    :monkey: monkey dictionary
    :monkeys: list with monkeys
    """
    if int(worry_level) % monkey["test"] == 0:
        monkeys[monkey["true"]]["items"].append(worry_level)
    else:
        monkeys[monkey["false"]]["items"].append(worry_level)


def monkey_inspection(monkey, monkeys):
    """
    Monkey item inspection

    :monkey: monkey dictionary
    :monkeys: list with monkeys
    """
    for item_num in range(0, len(monkey["items"])):
        worry_level = calculate_worry_level(monkey["items"].pop(0), monkey["operation"])
        # worry_level = bored_monkey(worry_level) # Part one calculation
        throws_an_item(worry_level, monkey, monkeys)
        monkey["inspected"] += 1


def get_lcm(monkeys):
    """
    Calculate the least common multiple for monkeys test

    :monkeys: list with monkeys
    :return: least common multiple for monkeys test
    """
    lcm = math.lcm(*[item["test"] for item in monkeys])
    return lcm


def monkey_business(monkeys):
    """
    Monkeys operations with items

    :monkeys: list with monkeys
    """
    monkey_round = 0
    lcm = get_lcm(monkeys)

    while monkey_round < 10000:  # Part two
        for monkey in monkeys:
            monkey_inspection(monkey, monkeys)
        # Recalculate values to make them manageble
        for monkey in monkeys:
            updated_items = []
            for item in monkey["items"]:
                item = item % lcm
                updated_items.append(item)
            monkey["items"].clear()
            monkey["items"] = updated_items

        monkey_round += 1


def monkeys_inspection():
    """
    Trigger solution for part 1 and part 2
    """
    print("Monkey business")
    monkeys = parse_input("input")
    add_number_of_inspected_items(monkeys)
    monkey_business(monkeys)
    print(monkeys)
    inspected_items = [n["inspected"] for n in monkeys]
    print(inspected_items)
    inspected_items.sort()
    print(inspected_items[-1] * inspected_items[-2])


if __name__ == "__main__":
    monkeys_inspection()
