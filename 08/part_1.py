# https://adventofcode.com/2025/day/08
import math
import collections


class Solution:
    def __init__(self):
        self.g = collections.defaultdict(set)
        self.distances = []
        self.nodes = []
        self.node_to_group_mapping = {}

    def _parse_input(self, s: str):
        rows = s.strip().split("\n")
        for row in rows:
            x, y, z = row.split(",")
            self.nodes.append((int(x), int(y), int(z)))

    def _calc_pairwise_distance(self, n1, n2):
        return math.sqrt((n1[0] - n2[0]) ** 2 + (n1[1] - n2[1]) ** 2 + (n1[2] - n2[2]) ** 2)

    def solve(self, s: str):
        self._parse_input(s)
        for i in range(len(self.nodes)):
            for j in range(i + 1, len(self.nodes)):
                self.distances.append((self._calc_pairwise_distance(self.nodes[i], self.nodes[j]), self.nodes[i], self.nodes[j]))

        self.distances.sort(key=lambda x: x[0])

        group_counter = 0
        for pair_index, (dist, i, j) in enumerate(self.distances):
            if pair_index == 1000:
                break

            # if in same group
            if (
                i in self.node_to_group_mapping
                and j in self.node_to_group_mapping
                and self.node_to_group_mapping[i] == self.node_to_group_mapping[j]
            ):
                continue

            # if one is in a group
            elif i in self.node_to_group_mapping and j not in self.node_to_group_mapping:
                self.node_to_group_mapping[j] = self.node_to_group_mapping[i]
                self.g[i].add(j)
                self.g[j].add(i)

            # if one is in a group
            elif j in self.node_to_group_mapping and i not in self.node_to_group_mapping:
                self.node_to_group_mapping[i] = self.node_to_group_mapping[j]
                self.g[i].add(j)
                self.g[j].add(i)

            # if neither in group
            elif j not in self.node_to_group_mapping and i not in self.node_to_group_mapping:
                group_counter += 1
                self.node_to_group_mapping[i] = group_counter
                self.node_to_group_mapping[j] = group_counter
                self.g[i].add(j)
                self.g[j].add(i)

            # if they're in different groups
            elif (
                i in self.node_to_group_mapping
                and j in self.node_to_group_mapping
                and self.node_to_group_mapping[i] != self.node_to_group_mapping[j]
            ):
                self.g[i].add(j)
                self.g[j].add(i)
                removed_group = self.node_to_group_mapping[j]
                for x in self.node_to_group_mapping:
                    if self.node_to_group_mapping[x] == removed_group:
                        self.node_to_group_mapping[x] = self.node_to_group_mapping[i]

            else:
                print("didnt expect to get here")

        counter = collections.defaultdict(int)

        for i in self.node_to_group_mapping:
            counter[self.node_to_group_mapping[i]] += 1

        group_sizes = list(counter.values())

        group_sizes.sort(reverse=True)
        mult = 1
        for i in group_sizes[:3]:
            mult *= i
        return mult
