# https://adventofcode.com/2025/day/03

"""
Two pointers approach. Since working l->r without substitution, can use greedy solution
"""


class Solution:
    def __init__(self):
        pass

    def _parse_input(self, s: str) -> list:
        banks = s.strip().split("\n")
        return [[int(x) for x in i] for i in banks]

    def solve(self, s: str):
        summed_joltage = 0
        parsed_input = self._parse_input(s)

        for line in parsed_input:
            l = 0
            r = 1
            max_seen = 0

            while r < len(line):
                max_seen = max(line[l] * 10 + line[r], max_seen)

                if line[r] > line[l]:
                    l = r

                r += 1

            summed_joltage += max_seen

        return summed_joltage
