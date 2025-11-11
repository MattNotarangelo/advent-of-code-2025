# Advent of Code 2025

Fork this

## Results

| Day                                        | Stars | Part 1                    | Part 2                    |
| ------------------------------------------ | ----- | ------------------------- | ------------------------- |
| [01](https://adventofcode.com/2025/day/1)  |       | [part_1.py](01/part_1.py) | [part_2.py](01/part_2.py) |
| [02](https://adventofcode.com/2025/day/2)  |       | [part_1.py](02/part_1.py) | [part_2.py](02/part_2.py) |
| [03](https://adventofcode.com/2025/day/3)  |       | [part_1.py](03/part_1.py) | [part_2.py](03/part_2.py) |
| [04](https://adventofcode.com/2025/day/4)  |       | [part_1.py](04/part_1.py) | [part_2.py](04/part_2.py) |
| [05](https://adventofcode.com/2025/day/5)  |       | [part_1.py](05/part_1.py) | [part_2.py](05/part_2.py) |
| [06](https://adventofcode.com/2025/day/6)  |       | [part_1.py](06/part_1.py) | [part_2.py](06/part_2.py) |
| [07](https://adventofcode.com/2025/day/7)  |       | [part_1.py](07/part_1.py) | [part_2.py](07/part_2.py) |
| [08](https://adventofcode.com/2025/day/8)  |       | [part_1.py](08/part_1.py) | [part_2.py](08/part_2.py) |
| [09](https://adventofcode.com/2025/day/9)  |       | [part_1.py](09/part_1.py) | [part_2.py](09/part_2.py) |
| [10](https://adventofcode.com/2025/day/10) |       | [part_1.py](10/part_1.py) | [part_2.py](10/part_2.py) |
| [11](https://adventofcode.com/2025/day/11) |       | [part_1.py](11/part_1.py) | [part_2.py](11/part_2.py) |
| [12](https://adventofcode.com/2025/day/12) |       | [part_1.py](12/part_1.py) | [part_2.py](12/part_2.py) |

## File structure
```txt
.
├─ runner.py           # helper function for running sample input
└─ template/
    └── main.py        # program entrypoint
    ├── part_1.py      # your part 1 solution
    ├── part_2.py      # your part 2 solution
    ├── question_input_part_1.txt
    ├── question_input_part_2.txt
    ├── sample_input_part_1.txt
    ├── sample_input_part_2.txt
    ├── sample_output_part_1.txt
    └── sample_output_part_2.txt
...
```

## Getting started

1. Copy template into a per-day folder (`cp -r template 01/`)
2. Copy sample input, sample output, and question input into their respective files
3. Write your solution in part_{n}.py
4. Run with `python3 01/main.py`

## How the runner works

This runs the `part_1.py` and `part_2.py` files with the relevant `sample_input_part_{x}.txt` input and confirms it matches against the `sample_output_part_{x}.txt` output. If the sample passes, then the `question_input_part_{x}.txt` input is used. The sample must pass in order to run the question input.
