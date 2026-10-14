import random
import sys
import time
from pathlib import Path

SOLUTION_PATH = Path("/app/sort.py")
MAX_VALUE = 10**7
MAX_COUNT = 10**5

sys.path.insert(0, "/app")
from sort import sort_numbers

def make_case(count, max_value, seed=0):
    """Return `count` random integers between 1 and `max_value`."""
    rng = random.Random(seed)
    return [rng.randint(1, max_value) for _ in range(count)]

def check(nums):
    result = sort_numbers(list(nums))
    assert result == sorted(nums)

def test_no_builtin_sorting():
    source = SOLUTION_PATH.read_text()
    for banned in ["sorted(", ".sort(", "heapq", "bisect"]:
        assert banned not in source, f"not allowed: {banned}"

def test_edge_cases():
    check([])
    check([5])
    check([2, 1])
    check([1, MAX_VALUE])
    check([MAX_VALUE, 1])

def test_random_sizes():
    for seed in range(10):
        check(make_case(count=seed * 50, max_value=MAX_VALUE, seed=seed))

def test_already_sorted_and_reversed():
    nums = make_case(count=10_000, max_value=MAX_VALUE, seed=2)
    check(sorted(nums))
    check(sorted(nums, reverse=True))

def test_full_size_is_reasonably_fast():
    nums = make_case(count=MAX_COUNT, max_value=MAX_VALUE, seed=3)
    start = time.perf_counter()
    check(nums)
    assert time.perf_counter() - start < 5, "too slow"
