# https://adventofcode.com/2025/day/02


class Solution:
    def __init__(self):
        pass

    def _parse_input(self, s: str) -> list:
        ranges = s.strip().split(",")
        return [i.split("-") for i in ranges]

    def solve(self, s: str):
        summed_ids = 0
        parsed_input = self._parse_input(s)
        for i in parsed_input:
            lower, upper = i
            for val in range(int(lower), int(upper) + 1, 1):
                if str(val)[: len(str(val)) // 2] == str(val)[len(str(val)) // 2 :]:
                    summed_ids += int(str(val)[: len(str(val))])

        return summed_ids
