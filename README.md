# Harbor tasks

A demo project for [Harbor](https://harborframework.com), a framework for evaluating AI agents. Each task gives an agent instructions and a Docker container to work in, then grades what the agent left behind.

## Tasks

### fast-sort

The agent must write `sort_numbers(nums)` in `/app/sort.py`: sort up to 100,000 integers between 1 and 10,000,000, as fast as possible, without the built-in sorting tools (`sorted`, `list.sort`, `heapq`, `bisect`).

Testing has two steps:

1. **Correctness:** pytest checks the output on edge cases, random inputs of various sizes and sorted or reversed input. Any failure gives a reward of 0.
2. **Benchmark:** if the output is correct, the solution and Python's built-in `sorted()` are both timed on 100,000 numbers. The results go to `reward.json`:
   - `reward`: 1 if correct, 0 if not
   - `solution_ms` and `builtin_sorted_ms`: best of 5 runs, in milliseconds
   - `speed_vs_builtin`: `builtin_sorted_ms / solution_ms`.

The reference solution in `solution/solve.sh` is a plain merge sort.

## Running

```bash
# Check the task itself with the reference solution (no API key needed)
harbor run -p fast-sort -a oracle

# Run a real agent
export ANTHROPIC_API_KEY=...
# Or add this key to env file as ANTHROPIC_API_KEY=...
harbor run -p fast-sort -a claude-code -m anthropic/claude-opus-5-5 --env-file .env
```

Results are stored in `jobs/`.

For reference, 2 outputs - one using the provided solve and one from an llm have also been included in the repository in jobs folder. (Otherwise this folder is ignored.)
