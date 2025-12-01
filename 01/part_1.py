# https://adventofcode.com/2025/day/01


class Solution:
    def __init__(self):
        self.pos = 50
        self.zero_count = 0

    def _parse_input(self, s: str) -> list:
        ret = []
        lines = s.strip().split("\n")
        for line in lines:
            direction = line[0]
            movement = line[1:]
            ret.append([direction, int(movement)])
        return ret

    def solve(self, s: str):
        parsed_input = self._parse_input(s)
        for i in parsed_input:
            if i[0] == "L":
                self.pos -= i[1]
            else:
                self.pos += i[1]

            self.pos %= 100

            if self.pos == 0:
                self.zero_count += 1
        return str(self.zero_count)
