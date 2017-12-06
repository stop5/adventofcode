#!/usr/bin/python3


def calculate_surface(h, w, l):
    f = h * w
    r = h * l
    t = w * l
    return min(f, r, t) + (f + r + t) * 2


def calculate_bow(h, w, l):
    f = h * w * 2
    r = h * l * 2
    return h * w * l + min(h + l, h + w, w + l) * 2


def traverse(data, computer):
    surface = 0
    for line in data:
        line = [int(a) for a in line.split("x")]
        surface += computer(*line)
    return surface


if __name__ == "__main__":
    with open("2") as dfile:
        data = dfile.readlines()
    print("Solution 1: ", traverse(data, calculate_surface))
    print("Solution 2: ", traverse(data, calculate_bow))
