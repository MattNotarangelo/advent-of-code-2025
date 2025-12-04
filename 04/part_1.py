# https://adventofcode.com/2025/day/04

PAPER = "@"
NO_PAPER = "."


class Solution:
    def __init__(self):
        self.data = []

    def _parse_input(self, s: str):
        rows = s.strip().split("\n")
        self.data = [list(i) for i in rows]

    def _contains_paper(self, x, y):
        if x < 0 or y < 0 or x >= len(self.data[0]) or y >= len(self.data):
            return False

        return self.data[y][x] == PAPER

    def _check_position(self, x, y):

        adjacent = (
            self._contains_paper(x + 1, y)
            + self._contains_paper(x + 1, y + 1)
            + self._contains_paper(x, y + 1)
            + self._contains_paper(x - 1, y + 1)
            + self._contains_paper(x - 1, y)
            + self._contains_paper(x - 1, y - 1)
            + self._contains_paper(x, y - 1)
            + self._contains_paper(x + 1, y - 1)
        )

        return adjacent < 4

    def solve(self, s: str):
        count = 0
        self._parse_input(s)
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                if self.data[y][x] == PAPER:
                    count += self._check_position(x, y)
        return count
