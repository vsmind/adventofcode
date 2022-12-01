def main():
    print("-----Read input-----")
    file = open("input", 'r')
    readfile = file.readlines()
    print("-----Read OK-----")
    # Starting conditions
    elf_count = 0
    elf_list = [0]
    for line in readfile:
        # If input is not empty add it value
        if line.strip():
            elf_list[elf_count] += int(line)
        # In other case add new elf to the list
        else:
            elf_list.append(0)
            elf_count += 1
    # Sort array of elf calories in descending order
    print("-----Elf calories list-----")
    print(elf_list)
    elf_list.sort(reverse=True)
    print("-----Sorted calories list-----")
    print(elf_list)
    top_calories = elf_list[0:3]
    print("Top three Elves calories")
    print(sum(top_calories))


if __name__ == "__main__":
    main()
