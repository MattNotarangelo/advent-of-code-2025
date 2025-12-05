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

        for ingredient in self.ingredients:
            fresh = False
            for lower_range, upper_range in self.ranges:
                if ingredient < lower_range:
                    continue

                fresh |= ingredient <= upper_range
            fresh_ingredients += fresh

        return fresh_ingredients
