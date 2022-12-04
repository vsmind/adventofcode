def sticker():
    file = open("input_test", 'r')
    cleanig_orders = file.readlines()

    assignment_pairs = 0
    for order in cleanig_orders:
        elfs_order = order.strip().split(",")
        # Parse sections
        first_elf_sections = elfs_order[0].split("-")
        second_elf_sections = elfs_order[1].split("-")
        # Create range from sections
        first_elf_orders = range(int(first_elf_sections[0]), int(first_elf_sections[1]) + 1)
        second_elf_orders = range(int(second_elf_sections[0]), int(second_elf_sections[1]) + 1)
        # Find if one order is the part of another
        same_orders = set(first_elf_orders).issubset(second_elf_orders) or set(second_elf_orders).issubset(first_elf_orders)
        if same_orders:
            assignment_pairs += 1
    print("Assignment pairs", assignment_pairs)


if __name__ == "__main__":
    sticker()
