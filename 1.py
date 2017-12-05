#!/usr/bin/python3


def sumoffset(text, offset=1):
    length = len(text)
    sum = 0
    for pos in range(length):
        if text[pos] == text[(pos + offset) % length]:
            sum += int(text[pos])
    return sum


if __name__ == "__main__":
    with open("1") as dfile:
        data = dfile.read()
    print("First solution: ", sumoffset(data))
    print("Second Solution: ", sumoffset(data, int(len(data) / 2)))
