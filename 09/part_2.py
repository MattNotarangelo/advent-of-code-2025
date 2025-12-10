# https://adventofcode.com/2025/day/09
import collections

# >:(


class Solution:
    def __init__(self):
        self.nodes = []
        self.vertical_ranges = collections.defaultdict(list)
        self.horizontal_ranges = collections.defaultdict(list)

    def _parse_input(self, s: str):
        rows = s.strip().split("\n")
        self.nodes = [tuple(map(int, line.split(","))) for line in rows]
        n = len(self.nodes)

        # Store segments
        for i in range(n):
            x1, y1 = self.nodes[i]
            x2, y2 = self.nodes[(i + 1) % n]

            if x1 == x2:
                self.vertical_ranges[x1].append((min(y1, y2), max(y1, y2)))
            else:
                self.horizontal_ranges[y1].append((min(x1, x2), max(x1, x2)))

    def _is_rectangle_valid(self, x_min, x_max, y_min, y_max):
        # Check vertical segments
        for x, segments in self.vertical_ranges.items():
            # Skip if vertical line is not strictly inside rectangle
            if not (x_min < x < x_max):
                continue

            # Check if any segment intersects the y-range
            for y_start, y_end in segments:
                # Segment overlaps if: end > y_min AND start < y_max
                if y_end > y_min and y_start < y_max:
                    return False

        # Check horizontal segments
        for y, segments in self.horizontal_ranges.items():
            # Skip if horizontal line is not strictly inside rectangle
            if not (y_min < y < y_max):
                continue

            # Check if any segment intersects the x-range
            for x_start, x_end in segments:
                # Segment overlaps if: end > x_min AND start < x_max
                if x_end > x_min and x_start < x_max:
                    return False

        return True

    def solve(self, s):
        self._parse_input(s)

        to_check = []
        n = len(self.nodes)

        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = self.nodes[i]
                x2, y2 = self.nodes[j]

                area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

                to_check.append((area, i, j))

        # Check rectangles in decreasing order of area (largest first)
        to_check.sort(key=lambda x: x[0], reverse=True)
        for area, i, j in to_check:
            x1, y1 = self.nodes[i]
            x2, y2 = self.nodes[j]

            # Check if this rectangle is valid
            if self._is_rectangle_valid(min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)):
                return area

        return 0
