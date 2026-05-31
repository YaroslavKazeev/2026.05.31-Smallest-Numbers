"""Placeholder for the three-smallest-distinct-numbers solution.

Implement the algorithm in `find_three_smallest_distinct_numbers`.
"""


def find_three_smallest_distinct_numbers(numbers):
    if not isinstance(numbers, (list, tuple)):
        raise TypeError("Input must be a list or tuple of numbers.")

    if len(numbers) < 3:
        raise ValueError("Array must contain at least three elements.")

    distinct_sorted = sorted(set(numbers))
    if len(distinct_sorted) < 3:
        raise ValueError("Array does not contain three distinct numbers.")

    return distinct_sorted[:3]


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
