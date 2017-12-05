#!/usr/bin/python3


def none(*args):
    return


def basement_hook(floor, instruction_pos):
    if floor < 0:
        return instruction_pos


def go(instructions, hook=none):
    floor = 0
    instruction_pos = 0
    for instruction in instructions:
        if instruction == "(":
            floor += 1
        elif instruction == ")":
            floor -= 1
        instruction_pos += 1
        if hook(floor, instruction_pos):
            return hook(floor, instruction_pos)
    return floor


if __name__ == "__main__":
    with open("1") as dfile:
        data = dfile.read()
    print("Solution 1: ", go(data))
    print("Solution 2: ", go(data, basement_hook))
