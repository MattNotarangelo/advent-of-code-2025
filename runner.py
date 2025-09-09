from typing import Callable
import time


def runner(name: str, f: Callable, path: str):

    sample_input = open(f"{path}/sample_input_part_{name}.txt").read().strip()
    expected_sample_output = open(f"{path}/sample_output_part_{name}.txt").read().strip()
    question_input = open(f"{path}/question_input_part_{name}.txt").read().strip()

    # time the sample run
    start = time.perf_counter_ns()
    actual_sample_output = f(sample_input)
    sample_elapsed = time.perf_counter_ns() - start

    samples_match = str(actual_sample_output) == expected_sample_output

    if samples_match:
        print(f"✅ part {name} sample passed in {get_ms(sample_elapsed)}ms")
    else:
        print(f"❌ part {name} sample FAILED in {get_ms(sample_elapsed)}ms")
        print(f"  > expected output: {expected_sample_output}")
        print(f"  > actual output: {actual_sample_output}")

    # sample must pass for question to run
    if samples_match:
        start_q = time.perf_counter_ns()
        actual_question_output = f(question_input)
        question_elapsed = time.perf_counter_ns() - start_q
        print(f"part {name} question output: {actual_question_output} in {get_ms(question_elapsed)}ms")


def get_ms(elapsed_ns: int) -> float:
    return elapsed_ns / 1_000_000
