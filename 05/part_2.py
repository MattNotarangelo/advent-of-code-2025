# https://adventofcode.com/2025/day/05


class Solution:
    def __init__(self):
        self.ranges = []
        self.ingredients = []

    def _parse_input(self, s: str):
        rows = s.strip().split("\n")
        for i in range(len(rows)):
            if rows[i] == "":
                ranges_raw = rows[:i]
                self.ingredients = rows[i + 1 :]
                break

        for i in ranges_raw:
            lower_range, upper_range = i.split("-")
            self.ranges.append((int(lower_range), int(upper_range)))

        self.ingredients = [int(i) for i in self.ingredients]

    def solve(self, s: str):
        fresh_ingredients = 0

        self._parse_input(s)
        self.ranges.sort(key=lambda x: x[0])

        consolidated_lower = self.ranges[0][0]
        consolidated_upper = self.ranges[0][1]
        i = 0
        while i < len(self.ranges) - 1:
            if consolidated_upper >= self.ranges[i + 1][0]:
                consolidated_upper = max(consolidated_upper, self.ranges[i + 1][1])
                i += 1
            else:
                fresh_ingredients += consolidated_upper - consolidated_lower + 1
                i += 1
                consolidated_lower = self.ranges[i][0]
                consolidated_upper = self.ranges[i][1]

        fresh_ingredients += consolidated_upper - consolidated_lower + 1

        return fresh_ingredients


"""
4-8
5-7
==============
1-11
19-24

"""
