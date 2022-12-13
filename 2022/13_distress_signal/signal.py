def parse_input(input_file):
    signal_file = []
    input_file = open(input_file, 'r')
    signal_combinations = input_file.read().split("\n\n")
    for combination in signal_combinations:
        c = combination.split("\n")
        signal_file.append([eval(c[0]), eval(c[1])])
    return signal_file


def compare(left, right):

    print("LEFT", left)
    print("RIGHT", right)

    if type(left) == int and type(right) == int:
        if left < right:
            return 1
        elif left == right:
            return 0
        else:
            return -1

    if type(left) == list and type(right) == list:
        if len(left) > 0 and len(right) > 0:
            for i in range(len(left)):
                # If we are out of elements in right array
                if len(right) == 0:
                    return -1

                result = compare(left.pop(0), right.pop(0))
                if result == 1:
                    return 1
                if result == -1:
                    return -1

        elif len(left) == 0:
            return 1
        elif len(right) == 0:
            return -1
    else:
        if type(left) == int:
            left = [ left ]
        else:
            right = [ right ]

        if len(left) == 0:
            return 1
        if len(right) == 0:
            return -1
        return compare(left.pop(0), right.pop(0))

    if len(left) == 0 and len(right) > 0:
        return 1

def check_signal(signal_file):
    sum_of_the_indices = []
    for i, pairs_of_packets in enumerate(signal_file):
        if compare(pairs_of_packets[0], pairs_of_packets[1]) == 1:
            print("OK", i+1)
            sum_of_the_indices.append(i+1)
    print("Sum_of_the_indices", sum(sum_of_the_indices))


def signal():
    signal_file = parse_input("input")
    print(signal_file[0][0])
    check_signal(signal_file)


if __name__ == "__main__":
    signal()
