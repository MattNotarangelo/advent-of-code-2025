# https://adventofcode.com/2025/day/11
import collections

START = "svr"
END = "out"
REQUIRED_NODES = ["dac", "fft"]


class Solution:
    def __init__(self):
        self.g = collections.defaultdict(set)
        self.mem = {}

    def _parse_input(self, s: str):
        rows = s.strip().split("\n")
        for row in rows:
            in_node, out_node = row.split(": ")
            out_nodes = out_node.split(" ")
            for i in out_nodes:
                self.g[in_node].add(i)

    def _dfs(self, curr, seen, seen_dac, seen_fft):
        if curr == END:
            return seen_dac and seen_fft

        if curr in seen:
            return 0

        if curr == REQUIRED_NODES[0]:
            seen_dac = 1
        if curr == REQUIRED_NODES[1]:
            seen_fft = 1

        mem_key = (curr, seen_dac, seen_fft)
        if mem_key in self.mem:
            return self.mem[mem_key]

        count = 0
        seen.add(curr)
        for i in self.g[curr]:
            count += self._dfs(i, seen, seen_dac, seen_fft)
        seen.remove(curr)

        self.mem[mem_key] = count
        return count

    def solve(self, s):
        path_count = 0
        self._parse_input(s)

        for i in self.g[START]:
            path_count += self._dfs(i, set(), False, False)

        return path_count
