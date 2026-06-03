"""Placeholder for the three-smallest-distinct-numbers solution.

Implement the algorithm in `find_three_smallest_distinct_numbers`.
"""


def find_three_smallest_distinct_numbers(nums):
    # Put your solution here
    if not isinstance(nums, (list, tuple)):
        raise TypeError("Input must be a list or tuple of numbers.")
    if len(nums) < 3:
        raise ValueError("Array must contain at least three elements.")
    else:
        looked = set(nums[0:3])
        window = sorted(list(looked))

        for i in range(3, len(nums)):
            if nums[i] not in looked:
                for j in range(len(window)):
                    if nums[i] < window[j]:
                        window.insert(j, nums[i])
                        window = window[0:3]
                        looked.add(nums[i])
                        break
                if len(window) < 3:
                    window.append(nums[i])
                    looked.add(nums[i])
    if len(window) < 3:
        raise ValueError("Array does not contain three distinct numbers.")
    return window


# Prepared use cases for implementation and testing (do not execute here).
USE_CASES = [
    {
        "input": [7, -1, 3, 4, 2, 6, 2],
        "expected": [-1, 2, 3],
        "description": "Typical case with duplicates and mixed order",
    },
    {
        "input": [9, 1],
        "expected_error": "Array must contain at least three elements.",
        "description": "Too few elements",
    },
    {
        "input": [2, 5, 5, 5],
        "expected_error": "Array does not contain three distinct numbers.",
        "description": "Not enough distinct numbers",
    },
]
