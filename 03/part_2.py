# https://adventofcode.com/2025/day/03

"""
Twelve pointers approach. Since reading l->r without substitution, can use greedy solution. O(N)
"""


class Solution:
    def __init__(self):
        self.parsed_input = []

    def _parse_input(self, s: str):
        ret = []
        banks = s.strip().split("\n")
        for i in banks:
            ret.append([int(x) for x in i])
        self.parsed_input = ret

    def _get_curr_joltage(self, indexes, line):
        # Not sure if python is faster at int addition or string conv lol
        total = ""
        for i in indexes:
            total += str(line[i])
        return int(total)

    def _search_within_range(self, l, target, lower, upper):
        i = lower
        while i <= upper:
            if l[i] == target:
                return i
            i += 1
        return 99999999999999

    def solve(self, s: str):
        summed_joltage = 0
        self._parse_input(s)

        for line in self.parsed_input:
            local_indexes = list(range(len(line) - 12, len(line)))

            for i, v in enumerate(local_indexes[:]):
                l = 0
                r = v
                if i > 0:
                    l = local_indexes[i - 1] + 1
                local_max = max(line[l : r + 1])
                local_indexes[i] = self._search_within_range(line, local_max, l, r + 1)

            summed_joltage += self._get_curr_joltage(local_indexes, line)

        return summed_joltage
