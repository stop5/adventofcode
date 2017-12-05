#!/usr/bin/python3
zahl = 265149
matrix = [[0 for a in range(21)] for a in range(21)]
x = 11
y = 11
debug = False


def gen_table(size):
    return [
        [
            0
            for a in range(size)
        ]
        for a in range(size)
    ]


def tablecenter(table):
    size = len(table)
    newtable = gen_table(size + 2)
    for line in range(1, size + 1):
        newtable[line] = [0, *table[line-1], 0]
    return newtable


def tableprint(table, lengthi=6):
    item = "{: " + str(lengthi) + "d}"
    for line in table:
        for column in line:
            print(item.format(column), end="")
        print()


def traverse(table, func, max, check):
    y = x = len(table) // 2
    pos = 0
    while True:
        length = len(table)
        if y + 1 <= length and x + 1 == length:  # nach rechts
            y += 1
        elif x - 1 >= 0 and table[x - 1][y] == 0:  # nach oben
            x -= 1
        elif y - 1 >= 0:  # Nach Links
            y -= 1
        else:  # Nach unten
            x += 1
        if x + 1 == length == y:
            table = tablecenter(table)
            x += 1
            y += 1
        pos += 1
        table[x][y] = func(table=table, x=x, y=y, position=pos)
        test = check(table[x][y], pos, max)
        if test:
            return table[x][y]


def compute_1(table, x, y, position):
    length = len(table)
    return x + y - length


def compute_2(table, x, y, position):
    value = 0
    for rpos in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
        try:
            value += table[x + rpos[0]][y + rpos[1]]
        except IndexError:
            pass
    return value


def check_1(value, position, maximum):
    return position == maximum


def check_2(value, position, maximum):
    return value >= maximum


if __name__ == "__main__":
    with open("3") as number_file:
        number = int(number_file.read())
    solution_1 = traverse([[1, ], ], compute_1, number, check_1)
    solution_2 = traverse([[1, ], ], compute_2, number, check_2)
    print("Solution 1: ", solution_1)
    print("Solution 1: ", solution_2)
