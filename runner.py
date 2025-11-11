from typing import Callable
import time


def runner(part_number: str, f: Callable, path: str):
    sample_input = open(f"{path}/sample_input_part_{part_number}.txt").read().strip()
    expected_sample_output = open(f"{path}/sample_output_part_{part_number}.txt").read().strip()
    question_input = open(f"{path}/question_input_part_{part_number}.txt").read().strip()

    # time the sample run
    actual_sample_output = f(sample_input)

    samples_match = str(actual_sample_output) == expected_sample_output

    if samples_match:
        print(f"part {part_number} sample passed ✅")
    else:
        print(f"part {part_number} sample FAILED ❌")
        print(f" > expected output: {expected_sample_output}")
        print(f" > actual output: {actual_sample_output}")

    # sample must pass for question to run
    if samples_match:
        actual_question_output = f(question_input)
        print(f"part {part_number} question output: {actual_question_output}")
