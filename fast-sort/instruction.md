# Fastest Sort

Create the file `/app/sort.py` with this function:

```python
def sort_numbers(nums: list[int]) -> list[int]:
    ...
```

It must return the numbers in ascending order.

- `nums` has between 0 and 100,000 integers.
- Each integer is between 1 and 10,000,000. Duplicates are allowed.
- Memory limit is 2048 MB.

Make it as fast as you can. Your solution is first checked for correctness, then timed.

## Rules

- Use only the Python standard library.
- Do not use the built-in sorting tools: `sorted`, `list.sort`, `heapq` or `bisect`.
