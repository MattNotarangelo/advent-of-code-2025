# https://adventofcode.com/2025/day/06


def multiply_items(v):
    a = 1
    for i in v:
        a *= int(i)
    return a


def sum_items(v):
    a = 0
    for i in v:
        a += int(i)
    return a


class Solution:
    def __init__(self):
        self.values = []
        self.operators = []

    def _parse_input(self, s: str):
        ret = []
        rows = s.strip().split("\n")
        operations = rows[-1]
        data = rows[:-1]

        for row in data:
            line = []
            row_values = row.split(" ")
            for i in row_values:
                if i.strip():
                    line.append(i.strip())

            ret.append(line)

        self.values = ret
        ret = []
        line = []
        row_values = operations.split(" ")
        for i in row_values:
            if i.strip():
                line.append(i.strip())

        self.operators = line

    def solve(self, s: str):
        count = 0

        self._parse_input(s)

        i = 0
        for v in zip(*self.values):
            if self.operators[i] == "+":
                count += sum_items(v)
            else:
                count += multiply_items(v)

            i += 1

        return count
