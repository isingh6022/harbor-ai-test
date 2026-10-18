import re
from collections import Counter

_NZ = re.compile(b"\x01")
_start = re.Match.start


def sort_numbers(nums: list[int]) -> list[int]:
    if len(nums) < 2:
        return list(nums)
    # Mark presence in a byte table; remember repeated occurrences separately.
    flags = bytearray(max(nums) + 1)
    extra = []
    add = extra.append
    for x in nums:
        if flags[x]:
            add(x)
        else:
            flags[x] = 1
    # Positions of set bytes, in ascending order, found by the C regex engine.
    uniq = list(map(_start, _NZ.finditer(flags)))
    if not extra:
        return uniq
    # Splice in the duplicates (few distinct values, or few occurrences).
    cnt = Counter(extra)
    out = []
    ext = out.extend
    idx = uniq.index
    prev = 0
    for d in sort_numbers(list(cnt)):
        i = idx(d, prev) + 1
        ext(uniq[prev:i])
        ext([d] * cnt[d])
        prev = i
    ext(uniq[prev:])
    return out
