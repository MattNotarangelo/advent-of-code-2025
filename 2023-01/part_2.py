# https://adventofcode.com/2023/day/01


WORDS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


class Solution:
    def __init__(self):
        self.data = []

    def _parse_input(self, s: str):
        rows = s.strip().split("\n")
        self.data = rows

    def solve(self, s: str):
        count = 0
        self._parse_input(s)

        for line in self.data:
            local = ""
            for i in range(len(line)):
                if line[i].isdigit():
                    local += str(line[i])
                    break
                else:
                    found = False
                    for word in WORDS:
                        if line[i : i + len(word)] == word:
                            local += str(WORDS[word])
                            found = True
                            break
                    if found == True:
                        break

            for i in range(len(line) - 1, -1, -1):
                if line[i].isdigit():
                    local += str(line[i])
                    break
                else:
                    found = False
                    for word in WORDS:
                        if line[i : i + len(word)] == word:
                            local += str(WORDS[word])
                            found = True
                            break
                    if found == True:
                        break
            count += int(local)

        return count
