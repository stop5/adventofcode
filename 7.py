#!/usr/bin/python3
import re
from pprint import pprint

lineformat = re.compile("(\w+) \((\d+)\)(?: -> ([\w, ]+))?")

class WeightItem:
    def __init__(self, name, data):
        for match in data:
            if match[1] == name:
                break
        self.name = match[1]
        self.weight = self.subweight = int(match[2])
        self.data = []
        if match[3]:
            for item in match[3].split(", "):
                item = WeightItem(item, data)
                self.data.append(item)
                self.subweight += item.subweight

    def balance_weight(self):
        if len(data) == 0:
            return False
        sw = {}
        weight = {}
        for item in self.data:
            balance =  item.balance_weight()
            if balance:
                return balance
            if item.subweight not in sw:
                sw.update({item.subweight: [0, item]})
            sw[item.subweight][0] += 1
        if len(sw) > 1:
            normal = max(sw.values(), key=lambda x:x[0])[1]
            outlier = min(sw.values(), key=lambda x:x[0])[1]
            return normal.subweight - outlier.subweight + outlier.weight
        return False

    def tree(self):
        return {self: [item.tree() for item in self.data]}

    def __repr__(self):
        return "<{} {} {}>".format(self.name, self.weight, self.subweight)

def get_top(data):
    bottoms = []
    for item in data:
        if item[3]:
            for b in item[3].split(", "):
                if b not in bottoms:
                    bottoms.append(b)
    for item in data:
        if item[1] not in bottoms:
            return item

if __name__ == "__main__":
    with open("7") as dfile:
        data = dfile.readlines()
        data = [lineformat.match(line) for line in data]
    top = get_top(data)
    top = WeightItem(top[1], data)
    print("Solution 1: ", top.name)
    print("Solution 2: ", top.balance_weight())
