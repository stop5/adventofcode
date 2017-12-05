#!/usr/bin/python3


def first_checksum(list):
    int_list = [int(a) for a in list]
    return max(int_list) - min(int_list)


def second_checksum(list):
    for maximum in list[::-1]:
        for minimum in list:
            fraction = int(maximum) / int(minimum)
            if fraction.is_integer() and fraction != 1:
                return int(fraction)


if __name__ == "__main__":
    with open("2") as dfile:
        data = dfile.readlines()
        data = [a.split() for a in data]
    print("First Checksum: ", sum([first_checksum(a) for a in data]))
    print("Second Checksum: ", sum([second_checksum(a) for a in data]))
