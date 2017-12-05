#!/usr/bin/python3


def echo(input):
    return input


def count_valid(data, anagrams=True):
    valid = 0
    if anagrams:
        sort = echo
    else:
        sort = sorted
    for line in data:
        words = []
        for word in line.split():
            if sort(word) not in words:
                words.append(sort(word))
            else:
                break
        else:
            valid += 1
    return valid


if __name__ == "__main__":
    with open("4") as dfile:
        data = dfile.readlines()
    print("Solution 1:", count_valid(data))
    print("Solution 2:", count_valid(data, False))
