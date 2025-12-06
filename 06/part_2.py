# https://adventofcode.com/2025/day/06


class Solution:
    def __init__(self):
        pass

    def solve(self, s: str):
        rows = [list(i) for i in s.strip().split("\n")]
        longest_row = 0
        for i in rows:
            longest_row = max(longest_row, len(i))

        # pad out truncated rows with spaces to ensure zip captures everything
        for i in range(len(rows)):
            if len(rows[i]) < longest_row:
                rows[i] += " " * (longest_row - len(rows[i]))

        count = 0
        local_count = 0
        operation = None
        for i in zip(*rows):
            # check if not separator row
            if any([j.strip() for j in i]):
                # use local_count to check for first row and store operation
                if local_count == 0:
                    operation = i[-1]
                    if operation == "*":
                        local_count = 1

                if operation == "+":
                    local_count += int("".join(i[:-1]))
                else:
                    local_count *= int("".join(i[:-1]))

            # if reached separator row, accumulate local_count
            else:
                count += local_count
                local_count = 0

        # no empty row for last set of values, so add manually
        count += local_count
        return count
