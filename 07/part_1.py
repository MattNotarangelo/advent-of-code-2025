# https://adventofcode.com/2025/day/07

SPLITTER = "^"
EMPTY = "."
BEAM = "|"


class Solution:
    def __init__(self):
        # self.mem = []
        self.values = []
        self.splits = 0

    def _parse_input(self, s: str):
        rows = s.strip().replace("S", "|").split("\n")
        parsed_rows = [list(i) for i in rows]
        self.values = parsed_rows

        self.mem = [[None] * len(self.values[0])] * len(self.values)

    def solve(self, s: str):
        self._parse_input(s)

        for y in range(1, len(self.values)):  # first row has source only
            for x in range(len(self.values[y])):
                if self.values[y][x] == EMPTY and self.values[y - 1][x] == BEAM:
                    self.values[y][x] = BEAM

                elif self.values[y][x] == SPLITTER and self.values[y - 1][x] == BEAM:
                    self.values[y][x - 1] = BEAM
                    self.values[y][x + 1] = BEAM
                    self.splits += 1

        return self.splits
