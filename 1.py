#!/usr/bin/python3


def sumoffset(text, offset=1):
    length = len(text)
    sum = 0
    for pos in range(length):
        if text[pos] == text[(pos + offset) % length]:
            sum += int(text[pos])
    return sum


if __name__ == "__main__":
    sum = 0
    data = ""
    with open("1") as input:
        data = input.read()
    print("First solution: ", sumoffset(data))
    print("Second Solution: ", sumoffset(data, int(len(data) / 2)))
