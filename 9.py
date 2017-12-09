#!/usr/bin/python3


if __name__ == "__main__":
    with open("9") as dfile:
        data = dfile.read()
    counter = 0
    depth = 0
    score = 0
    garbage = False
    garbagecounter = 0
    while counter < len(data):
        if data[counter] == "!":
            counter += 2
            continue
        elif garbage and data[counter] != ">":
            garbagecounter += 1
        elif garbage and data[counter]  == ">":
            garbage = False
        elif data[counter]  == "<":
            garbage = True
        elif data[counter]  == "{":
            depth += 1
            score += depth
        elif data[counter]  == "}":
            depth -= 1
        counter += 1
    print("Solution 1:", score)
    print("Solution 2:", garbagecounter)
