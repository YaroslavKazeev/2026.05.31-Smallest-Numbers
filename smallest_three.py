"""Placeholder for the three-smallest-distinct-numbers solution.

Implement the algorithm in `find_three_smallest_distinct_numbers`.
"""


def find_three_smallest_distinct_numbers(nums):
    # Put your solution here
    if len(nums) < 3:
        raise Exception("Array must contain at least three elements.")
    elif len(set(nums)) < 3:
        raise Exception("Array does not contain three distinct numbers.")
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
