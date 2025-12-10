# https://adventofcode.com/2025/day/09
import math
import collections
import heapq


class Solution:
    def __init__(self):
        self.nodes = []

    def _parse_input(self, s: str):
        rows = s.strip().split("\n")
        for row in rows:
            x, y = row.split(",")
            self.nodes.append((int(x), int(y)))

    def solve(self, s):
        max_seen = 0
        self._parse_input(s)
        for i in range(len(self.nodes)):
            for j in range(i + 1, len(self.nodes)):
                i_x, i_y = self.nodes[i]
                j_x, j_y = self.nodes[j]
                product = (abs(i_x - j_x) + 1) * (abs(i_y - j_y) + 1)
                max_seen = max(max_seen, product)

        return max_seen
