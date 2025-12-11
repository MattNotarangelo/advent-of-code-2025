# https://adventofcode.com/2025/day/11
import collections

START = "you"
END = "out"


class Solution:
    def __init__(self):
        self.g = collections.defaultdict(set)

    def _parse_input(self, s: str):
        rows = s.strip().split("\n")
        for row in rows:
            in_node, out_node = row.split(": ")
            out_nodes = out_node.split(" ")
            for i in out_nodes:
                self.g[in_node].add(i)

    def _dfs(self, curr, seen):
        if curr == END:
            return 1

        if curr in seen:
            return 0

        count = 0
        seen.add(curr)
        for i in self.g[curr]:
            count += self._dfs(i, seen)
        seen.remove(curr)

        return count

    def solve(self, s):
        path_count = 0
        self._parse_input(s)

        for i in self.g[START]:
            path_count += self._dfs(i, set())

        return path_count
