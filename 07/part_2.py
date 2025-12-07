# https://adventofcode.com/2025/day/07

SPLITTER = "^"
EMPTY = "."
BEAM = "|"


class Solution:
    def __init__(self):
        self.mem = []
        self.values = []
        self.splits = 0

    def _parse_input(self, s: str):
        rows = s.strip().replace("S", "|").split("\n")
        parsed_rows = [list(i) for i in rows]
        self.values = parsed_rows

        self.mem = [[0 for _ in range(len(self.values[0]))] for _ in range(len(self.values))]

    def _dp(self, y: int, x: int) -> int:
        if y == len(self.values) - 1:
            return 1

        if self.mem[y][x] > 0:
            return self.mem[y][x]

        splits = 0
        if self.values[y + 1][x] == EMPTY:
            splits += self._dp(y + 1, x)

        elif self.values[y + 1][x] == SPLITTER:
            splits += self._dp(y + 1, x - 1)
            splits += self._dp(y + 1, x + 1)

        self.mem[y][x] = splits
        return splits

    def solve(self, s: str):
        self._parse_input(s)

        splits = 0
        for x in range(len(self.values[0])):
            if self.values[0][x] == BEAM:
                splits += self._dp(0, x)
        return splits
