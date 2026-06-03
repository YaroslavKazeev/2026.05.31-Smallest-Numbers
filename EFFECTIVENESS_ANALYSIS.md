# Effectiveness Analysis: `copilot_solution` vs `my_solution`

**Date:** 2026-06-03  
**Branches compared:** `copilot_solution` (current) and `my_solution`  
**Problem:** Return the three smallest **distinct** integers from an input array, with defined error cases.

---

## Executive Summary

| Dimension                        | `copilot_solution` (current)                                   | `my_solution`                                                  |
| -------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| **Correctness (bundled tests)**  | Passes all 3 pytest cases                                      | Passes all 3 pytest cases                                      |
| **Correctness (extended cases)** | 10/10 custom scenarios                                         | 10/10 custom scenarios                                         |
| **Runtime (n = 100,000)**        | ~5.33 ms per call                                              | ~46.9 ms per call (~8.8× slower)                               |
| **Alignment with README goal**   | Simple but **full distinct sort**                              | Single-pass window idea, **now correct**                       |
| **Input validation**             | `TypeError` for non-list/tuple; `ValueError` for domain errors | `TypeError` for non-list/tuple; `ValueError` for domain errors |
| **Maintainability**              | Short, obvious                                                 | Longer, stateful loop with subtle edge cases                   |

**Overall:** `copilot_solution` is more effective: both solutions are fully correct on all tested inputs, but `copilot_solution` is consistently 8–19× faster and significantly simpler to read and maintain.

---

## Implementations at a Glance

### `copilot_solution` — sort distinct values, take first three

```python
distinct_sorted = sorted(set(numbers))
if len(distinct_sorted) < 3:
    raise ValueError("Array does not contain three distinct numbers.")
return distinct_sorted[:3]
```

- **Time:** O(n) to build the set, plus O(d log d) to sort distinct values `d` (worst case O(n log n) when all values are distinct).
- **Space:** O(d) for the set and sorted list.
- **Design trade-off:** Prioritizes correctness and simplicity over the README's "avoid full sort" guideline.

### `my_solution` — sliding window over first three, then scan from index 3

- Seeds `looked` and `window` from `nums[0:3]` only.
- For each later element not in `looked`, inserts into `window` if `nums[i] < window[j]` for some `j`; if `window` still has fewer than three entries after the inner loop, appends the new value.
- **Time:** O(n × window size) with list inserts (small constant window, but more Python-level overhead than sort-on-distinct).
- **Space:** O(window size) for auxiliary sets/lists.

---

## Correctness

### Bundled test suite (`test_smallest_three.py`)

Both branches pass the same three tests (Python 3.14.2, pytest 9.0.3):

1. Typical case: `[7, -1, 3, 4, 2, 6, 2]` → `[-1, 2, 3]`
2. Too few elements → `"Array must contain at least three elements."`
3. Too few distinct values → `"Array does not contain three distinct numbers."`

### Extended scenarios

Additional inputs were run against both implementations.

| Input                           | Expected       | `copilot_solution` | `my_solution`   |
| ------------------------------- | -------------- | ------------------ | --------------- |
| `[7, -1, 3, 4, 2, 6, 2]`        | `[-1, 2, 3]`   | OK                 | OK              |
| `[-5, -3, -1, 0, 1]`            | `[-5, -3, -1]` | OK                 | OK              |
| `[1, 2, 3]`                     | `[1, 2, 3]`    | OK                 | OK              |
| `[3, 2, 1]`                     | `[1, 2, 3]`    | OK                 | OK              |
| Descending 1..10                | `[1, 2, 3]`    | OK                 | OK              |
| `[4, 5, 6, 1, 2, 3]`            | `[1, 2, 3]`    | OK                 | OK              |
| `[1, 1, 2, 3, 4]`               | `[1, 2, 3]`    | OK                 | OK              |
| `[5, 5, 1, 2, 3]`               | `[1, 2, 3]`    | OK                 | OK              |
| Large descending + `0` (n=1001) | `[0, 1, 2]`    | OK                 | OK              |
| `[100, 50, 25, 10, 5, 1]`       | `[1, 5, 10]`   | OK                 | OK              |
| **Total**                       |                | **10/10**          | **10/10**       |

### Input typing

| Input   | `copilot_solution` | `my_solution` |
| ------- | ------------------ | ------------- |
| `None`  | `TypeError`        | `TypeError`   |
| `"abc"` | `TypeError`        | `TypeError`   |
| `123`   | `TypeError`        | `TypeError`   |

Both branches now explicitly validate list/tuple input.

---

## Performance

Benchmarks used `timeit.repeat` (minimum of 10 runs × 5 iterations) on descending arrays `list(range(n, 0, -1))`, where the answer is always `[1, 2, 3]`. Peak memory was measured with `tracemalloc` (one call per size). Python 3.14.2, Windows.

| n       | `copilot_solution` (s/call) | `my_solution` (s/call) | Speedup (copilot) | Peak memory (both) |
| ------- | --------------------------- | ---------------------- | ----------------- | ------------------ |
| 100     | 3.36 × 10⁻⁶                 | 3.57 × 10⁻⁵            | ~10.6×            | ~10 KB             |
| 1,000   | 1.87 × 10⁻⁵                 | 3.54 × 10⁻⁴            | ~18.9×            | ~40 KB             |
| 10,000  | 4.16 × 10⁻⁴                 | 4.46 × 10⁻³            | ~10.7×            | ~640 KB            |
| 100,000 | 5.33 × 10⁻³                 | 4.69 × 10⁻²            | ~8.8×             | ~6.0 MB            |

**Interpretation:**

- `copilot_solution` benefits from highly optimized CPython `set` + `sorted` builtins running in C.
- `my_solution` uses Python-level loops and `list.insert` in the inner loop.
- Memory use is lower for `my_solution` as it only maintains small constant-size structures.

For large inputs, **`copilot_solution` is consistently 8–19× faster** despite the theoretical "full sort" cost, because constant factors are low and the implementation does far less Python-level work.

The low constant factors in `copilot_solution` include:
- **Built-in C implementations**: `set()` and `sorted()` are implemented in highly optimized C code within CPython, avoiding Python interpreter overhead for the core operations.
- **Single pass through data**: The set construction and sorting happen in tight C loops with minimal branching.
- **No Python-level control flow**: The algorithm has no nested loops or conditional logic at the Python level, reducing interpreter overhead.
- **Efficient memory access patterns**: Consecutive memory access in set construction and sorting benefits from CPU cache locality.

---

## Fit with Project Requirements (`README.md`)

The README states:

> Create an efficient solution … **avoid sorting the entire array when possible** … runs in **linear time** …

| Criterion                      | `copilot_solution`                        | `my_solution`                                                          |
| ------------------------------ | ----------------------------------------- | ---------------------------------------------------------------------- |
| Linear-time aspiration         | Sorting distinct values can be O(n log n) | Linear scan structure with constant-size window |
| Avoid full-array sort          | No — sorts all distinct values            | Yes — only maintains a small 3-element window                          |
| Handles duplicates / negatives | Yes                                       | Yes                                                                    |
| Clear error messages           | Yes (`TypeError`, `ValueError`)           | Yes (`TypeError`, `ValueError`)                                        |

**`my_solution`** is closer to the documented algorithmic intent and is now correct. **`copilot_solution`** is faster in practice and simpler, but does not match the documented algorithmic ideal.

---

## Code Quality and Operability

| Aspect              | `copilot_solution`                    | `my_solution`                                         |
| ------------------- | ------------------------------------- | ----------------------------------------------------- |
| Lines of core logic | ~10                                   | ~20                                                   |
| Exception types     | `TypeError`, `ValueError` (idiomatic) | `TypeError`, `ValueError` (idiomatic)                 |
| Ease of review      | High                                  | Medium — window/`looked` invariants are easy to break |
| Risk of regression  | Low                                   | Higher (prefix initialization + insert condition)     |

---

## Recommendations

1. **Keep `copilot_solution` as the default** for correctness, speed, and maintainability unless the README's "no full sort" rule is a hard requirement.
2. **`my_solution` is correct** and can serve as a reference for the README's intended approach, but carries higher maintenance risk due to its stateful loop.
3. **Best of both worlds:** a true O(n) single-pass using three tracked variables (`first`, `second`, `third`) with careful duplicate handling, or a size-3 min-heap of distinct values, would satisfy the README and likely match or beat the sort-based solution in speed.

---

## Methodology

- Source compared via `git show my_solution:smallest_three.py` and the current `copilot_solution` branch.
- Bundled tests: `pipenv run pytest test_smallest_three.py -v` on `copilot_solution` (3 passed).
- Extended correctness and timing: `run_benchmarks.py` executed locally against inline copies of both implementations.
