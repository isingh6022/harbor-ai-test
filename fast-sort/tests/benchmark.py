"""Time sort_numbers on full-size inputs and write the results to reward.json.

Only run after the correctness tests pass. Usage: python benchmark.py <reward>
"""

import json
import sys
import time

from test_outputs import MAX_COUNT, MAX_VALUE, make_case, sort_numbers

RUNS = 5


def best_time(sort_fn, nums):
    """Fastest of multiple runs, in milliseconds."""
    times = []
    for _ in range(RUNS):
        data = list(nums)
        start = time.perf_counter()
        sort_fn(data)
        times.append(time.perf_counter() - start)
    return min(times) * 1000


nums = make_case(count=MAX_COUNT, max_value=MAX_VALUE, seed=42)
solution_ms = best_time(sort_numbers, nums)
builtin_ms = best_time(sorted, nums)

results = {
    "reward": int(sys.argv[1]),
    "solution_ms": round(solution_ms, 3),
    "builtin_sorted_ms": round(builtin_ms, 3),
    # Relative speed of the solution.
    "speed_vs_builtin": round(builtin_ms / solution_ms, 4),
}
print(json.dumps(results, indent=2))

with open("/logs/verifier/reward.json", "w") as f:
    json.dump(results, f, indent=2)
