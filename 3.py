#!/usr/bin/python3


def deliver(directions, robo=False):
    santapos = [0, 0]
    robopos = santapos[:]
    houses = [tuple(santapos), ]
    santa = True
    for direction in directions:
        if robo:
            if santa:
                pos = santapos
            else:
                pos = robopos
            santa = not santa
        else:
            pos = santapos
        if direction == 60:
            pos[0] -= 1
        elif direction == 62:
            pos[0] += 1
        elif direction == 94:
            pos[1] += 1
        elif direction == 118:
            pos[1] -= 1
        if tuple(pos) not in houses:
            houses.append(tuple(pos))
    return len(houses)


if __name__ == "__main__":
    with open("3", "br") as dfile:
        data = dfile.read()
    print("Solution 1: ", deliver(data))
    print("Solution 1: ", deliver(data, True))
