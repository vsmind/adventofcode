from functools import cmp_to_key


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
        if len(left) == 0 and len(right) == 0:
            return 0
        if len(left) == 0:
            return 1
        if len(right) == 0:
            return -1

        result = compare(left[0], right[0])
        return result if result != 0 else compare(left[1:], right[1:])
    else:
        if type(left) == int:
            left = [ left ]
        else:
            right = [ right ]

        return compare(left, right)


def check_signal(signal_file):
    sum_of_the_indices = []
    correct_package = []
    for i, pairs_of_packets in enumerate(signal_file):
        correct_package.append(pairs_of_packets[0])
        correct_package.append(pairs_of_packets[1])
        if compare(pairs_of_packets[0], pairs_of_packets[1]) == 1:
            position = i + 1
            print("OK", position)
            sum_of_the_indices.append(position)
        print("__________________________________")
    print("Sum_of_the_indices", sum(sum_of_the_indices)) # 6165 Too high # 6128 Too high # 5859 Too low
    print(correct_package)
    correct_package.extend([[[2]], [[6]]])
    pairs_sorted = sorted(correct_package, key=cmp_to_key(compare), reverse=True) # https://www.geeksforgeeks.org/how-does-the-functools-cmp_to_key-function-works-in-python/
    print(pairs_sorted)
    decoder_key_1 = pairs_sorted.index([[2]]) + 1
    decoder_key_2 = pairs_sorted.index([[6]]) + 1
    print(decoder_key_1, decoder_key_2)
    print("Decoder code", decoder_key_1 * decoder_key_2)


def signal():
    signal_file = parse_input("input_d.txt")
    check_signal(signal_file)


if __name__ == "__main__":
    signal()
