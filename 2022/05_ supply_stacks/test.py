import re


def test():
    line = "move 28 from 4 to 6"
    l = re.sub('[^0-9 _]', '', line).strip().split("  ")
    print(l)


if __name__ == "__main__":
    test()