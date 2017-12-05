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
        wörter = []
        for wort in line.split():
            if sort(wort) not in wörter:
                wörter.append(sort(wort))
            else:
                break
        else:
            valid += 1
    return valid


if __name__ == "__main__":
    with open("4") as dfile:
        data = dfile.readlines()
    print("Lösung 1:", count_valid(data))
    print("Lösung 2:", count_valid(data, False))
