#!/usr/bin/python3
import re
linereg = re.compile("(\w+) (inc|dec) (-?\d+) if (\w+) (\>|<|>=|<=|==|!=) (-?\d+)")

def parse(line):
    match = linereg.match(line)
    if match[2] == "inc":
        modify = 0 + int(match[3])
    else:
        modify = 0 - int(match[3])
    return {
        "output": match[1],
        "modify": modify,
        "input": match[4],
        "condition": match[5],
        "value": int(match[6]),
    }

def compute(data):
    vars = {}
    for line in data:
        line = parse(line)
        if line["output"] not in vars:
            vars.update({line["output"]: 0})
        if line["input"] not in vars:
            vars.update({line["input"]: 0})
        condition = False
        if line["condition"] == "<":
            if vars[line["input"]] < line["value"]:
                condition = True
        elif line["condition"] == ">":
            if vars[line["input"]] > line["value"]:
                condition = True
        elif line["condition"] == ">=":
            if vars[line["input"]] >= line["value"]:
                condition = True
        elif line["condition"] == "<=":
            if vars[line["input"]] <= line["value"]:
                condition = True
        elif line["condition"] == "==":
            if vars[line["input"]] == line["value"]:
                condition = True
        elif line["condition"] == "!=":
            if vars[line["input"]] != line["value"]:
                condition = True
        else:
            print(line)
        if condition == True:
            vars[line["output"]] += line["modify"]
        yield vars[line["output"]]
    return vars

def highest_ever(data):
    maximum = 0
    for iteration in compute(data):
        if type(iteration) == int:
            if iteration > maximum:
                maximum = iteration
    return maximum

def highest_end(data):
    computer = compute(data)
    while True:
        try:
            next(computer)
        except StopIteration as end:
            return max(end.value.values())



if __name__ == "__main__":
    with open("8") as dfile:
        data = dfile.readlines()
    print("Solution 1:", highest_end(data))
    print("Solution 2:", highest_ever(data))
