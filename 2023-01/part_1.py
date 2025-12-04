# https://adventofcode.com/2023/day/01


class Solution:
    def __init__(self):
        self.data = []

    def _parse_input(self, s: str):
        rows = s.strip().split("\n")
        self.data = [list(i) for i in rows]

    def solve(self, s: str):
        count = 0
        self._parse_input(s)

        for line in self.data:
            local = ""
            for v in line:
                if v.isdigit():
                    local += str(v)
                    break
            for v in line[::-1]:
                if v.isdigit():
                    local += str(v)
                    break
            count += int(local)

        return count
