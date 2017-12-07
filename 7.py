#!/usr/bin/python3
import re
from pprint import pprint
import copy

def deeplevel(subtree, i=0):
    level = 0
    maximum = [0, {}]
    if len(subtree) > 0:
        level += 1
        for node in subtree:
            if subtree[node] is None:
                pass
            elif type(subtree[node][1]) == list:
                level += 1
            else:
                temp = deeplevel(subtree[node][1], i+1)
                if temp > maximum[0]:
                    maximum = [temp, subtree[node][1]]
    return level + maximum[0] + i

def multiply(tree, multi, leafnodes):
    leaf = []
    for item in tree:
        if tree[item] is None:
            l = [item, [*multi, leafnodes[item]]]
            l.append(sum(l[1]))
            leaf.append(l)
        elif type(tree[item][1]) == dict:
            leaf.extend(multiply(tree[item][1], [*multi, tree[item][0]], leafnodes))
        else:
            for sitem in tree[item][1]:
                l = [sitem, [*multi,tree[item][0], leafnodes[sitem]]]
                l.append(sum(l[1]))
                leaf.append(l)
    return leaf

with open("7") as open_file:
    data = open_file.read().splitlines()
    test = re.compile("(\w+) \((\d+)\)(?: -> ([\w, ]+))?")
    topnodes = {}
    subnodes = {}
    for node in data:
        match = test.match(node).groups()
        if not (match[2] is None):
            combo = {match[0]: [int(match[1]), match[2]]}
            topnodes.update(combo)
        else:
            subnodes.update({match[0]: int(match[1])})
    for node in copy.deepcopy(topnodes):
        topnodes[node][1] = topnodes[node][1].split(", ")
        nsub = {}
        for counter in range(len(topnodes[node][1])):
            if topnodes[node][1][counter] in topnodes:
                nsub.update({topnodes[node][1][counter]: topnodes[topnodes[node][1][counter]]})
            else:
                nsub.update({topnodes[node][1][counter]: None})
        topnodes[node][1] = nsub
    deepest = {}
    for node in topnodes:
        deeplevelold = deeplevel(deepest)
        deeplevelnew = deeplevel({node: topnodes[node]})
        if deeplevelold < deeplevelnew:
            deepest = {node: topnodes[node]}
    print(list(deepest.keys())[0])
    pprint(multiply(deepest, [], subnodes))
