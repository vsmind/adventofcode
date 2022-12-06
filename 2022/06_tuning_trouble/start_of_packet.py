from collections import Counter


def start_packet_position():
    """
    Solution for part one and two
    """
    file = open("input", 'r')
    elf_signal = file.readlines()
    for line in elf_signal:
        print("First start-of-packet marker", find_start(4, line))
        print("First start-of-message marker", find_start(14, line))


def find_start(sequence, line):
    """
    Find out position of the sequence with X unique elements

    :sequence: number of unique elements in sequence
    :line: string to evaluate
    """
    for i, char in enumerate(line):
        start_of_packet = line[i:i + sequence]
        if len(Counter(start_of_packet)) == sequence:
            return i + sequence


if __name__ == "__main__": # 2615 to low
    start_packet_position()
