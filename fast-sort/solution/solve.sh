#!/bin/bash
# Reference (oracle) solution: writes a working /app/sort.py.
# It is a simple merge sort, meant to be correct and easy to read, not fast.
set -euo pipefail

cat > /app/sort.py <<'EOF'
def merge(left_half, right_half):
    merged = []
    left_index = 0
    right_index = 0

    # Repeatedly take the smaller front item from the two lists.
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            merged.append(left_half[left_index])
            left_index += 1
        else:
            merged.append(right_half[right_index])
            right_index += 1

    merged.extend(left_half[left_index:])
    merged.extend(right_half[right_index:])
    return merged

def sort_numbers(nums):
    if len(nums) <= 1:
        return list(nums)

    middle = len(nums) // 2
    sorted_left = sort_numbers(nums[:middle])
    sorted_right = sort_numbers(nums[middle:])

    return merge(sorted_left, sorted_right)
EOF
