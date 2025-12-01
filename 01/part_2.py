# https://adventofcode.com/2025/day/01


class Solution:
    def __init__(self):
        self.pos = 50
        self.zero_count = 0

    def _parse_input(self, s: str) -> list:
        ret = []
        lines = s.strip().split("\n")
        for line in lines:
            ret.append([line[0], int(line[1:])])
        return ret

    def solve(self, s: str):
        parsed_input = self._parse_input(s)
        for direction, movement in parsed_input:
            start_pos = self.pos
            step = -movement if direction == "L" else movement

            self.pos += step
            if step >= 0:
                self.zero_count += self.pos // 100
            else:
                self.zero_count += ((start_pos - 1) // 100) - ((self.pos - 1) // 100)  # evil

            self.pos %= 100

        return str(self.zero_count)
