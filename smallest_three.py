"""Placeholder for the three-smallest-distinct-numbers solution.

Implement the algorithm in `find_three_smallest_distinct_numbers`.
"""


def find_three_smallest_distinct_numbers(numbers):
    # Put your solution here
    if len(numbers) < 3:
        raise Exception("Array must contain at least three elements.")
    elif len(set(numbers)) < 3:
        raise Exception("Array does not contain three distinct numbers.")

    smallest = []
    return smallest


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
