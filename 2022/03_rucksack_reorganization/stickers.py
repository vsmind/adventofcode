item_priority = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def sticker():
    file = open("input", 'r')
    bags = file.readlines()

    bag_number = 1
    bag_set = set()
    # Code result
    sum_of_priorities = 0
    for line in bags:
        bag = line.strip()
        match bag_number % 3:
            case 1:  # Bag of the first elf
                # Add items from bag 1 to set collection
                bag_set.update(bag)
            case 2:  # Bag of the second elf
                # Add bag2
                bag2_set = set(bag)
                # Find the same items in bag1 and bag2
                item = bag_set.intersection(bag2_set)
                # Clear collection
                bag_set.clear()
                # Add same items to the collection
                bag_set.update(item)
            case 0:  # All 3 bags
                # Add bag 3
                bag3_set = set(bag)
                # Find the same item in all bags
                item = bag_set.intersection(bag3_set)
                # Calculate priority for items
                sum_of_priorities += item_priority.find(item.pop())
                # Clear items set collection
                bag_set.clear()
        # Increase bag number
        bag_number += 1
    # Print result
    print("Sum of priorities: ", sum_of_priorities)


if __name__ == "__main__":
    sticker()
