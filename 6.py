#!/usr/bin/python3


def reallocation(data, repeated=False):
    config = [int(a) for a in data]
    past = []
    distribute = 0
    pos = 0
    seen = False
    while True:
        while distribute:
            pos = (pos + 1) % len(data)
            config[pos] += 1
            distribute -= 1
        else:
            if tuple(config) in past:
                if not b or seen:
                    break
                else:
                    past = []
                    seen = True
            past.append(tuple(config))
            for pos in range(len(config)):
                if config[pos] == max(config):
                    distribute = config[pos]
                    config[pos] = 0
                    break
    return len(past)


if __name__ == "__main__":
    with open("6") as dfile:
        data = dfile.read().split()
    print("Solution 1: ", reallocation(data))
    print("Solution 2: ", reallocation(data, True))
