def traverse(data, jumpcomputer):
    line = 0
    jumps = 0
    try:
        while True:
            jump = int(data[line])
            data[line] = jumpcomputer(jump)
            line += jump
            jumps += 1
    except IndexError:
        return jumps


if __name__ == "__main__":
    with open("5") as dfile:
        data = dfile.readlines()
    print("Solution 1:", traverse(data[:], computer_1))
    print("Solution 2:", traverse(data[:], computer_2))
