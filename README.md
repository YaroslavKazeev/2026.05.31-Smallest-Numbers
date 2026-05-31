# Finding the Three Smallest Numbers in an Array

## Objective

Create an efficient solution that identifies the three smallest distinct numbers in an array of integers. The solution should avoid sorting the entire array when possible and should handle duplicates, negative numbers, and small input sizes gracefully.

## Use Cases

- Standard input with more than three distinct values with duplicates.
  - Input: `[7, -1, 3, 4, 2, 6, 2]`
  - Output: `[-1, 2, 3]`

## Edge Cases

- Arrays with fewer than three elements.
  - Example: `[9, 1]`
  - Expected: `Error: Array must contain at least three elements.`
- Arrays with less than three distinct elements.
  - Example: `[2, 5, 5, 5]`
  - Expected: `Error: Array does not contain three distinct numbers.`

## Efficiency

This approach runs in linear time with respect to the number of elements, with only a small constant amount of extra work for tracking up to three values. It avoids sorting the entire array.

## Deliverables

- A concise algorithm description.
- A Python implementation stub in `smallest_three.py`.
- Example use cases and edge cases in this README.

## Optional Challenge

Extend the same idea to find the `k` smallest distinct numbers by tracking up to `k` values instead of just three.
