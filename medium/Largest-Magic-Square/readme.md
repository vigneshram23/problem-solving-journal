# Largest Magic Square 

## 🧩 Problem Statement

A **k × k magic square** is a square grid where:
- All row sums are equal
- All column sums are equal
- Both diagonal sums are equal

Every `1 × 1` grid is trivially a magic square.

Given an `m × n` integer grid, return the **largest possible side length `k`**
of a magic square found in the grid.

---

## ✅ Example

### Input
```text
grid = [
  [7,1,4,5,6],
  [2,5,1,6,4],
  [1,5,4,3,2],
  [1,2,7,3,4]
]

Output
3
``` 

## Approach
Key Optimizations
Use prefix sums for rows and columns to compute sums in O(1)
Iterate square sizes from largest to smallest
Stop early once a valid magic square is found

## Validation Per Square
All row sums match
All column sums match
Main diagonal sum matches
Anti-diagonal sum matches

## ⏱ Complexity
| Metric | Value          |
| ------ | -------------- |
| Time   | `O(min(m,n)³)` |
| Space  | `O(m × n)`     |

Given constraints (m, n ≤ 50), this is efficient and passes all test cases.

## Usage
from solution import Solution
grid = [
    [5,1,3,1],
    [9,3,3,1],
    [1,3,3,8]
]

print(Solution().largestMagicSquare(grid))  # Output: 2


📌 Key Learnings
Prefix sum techniques for 2D grids
Efficient sliding window validation
Early termination optimization
Clean separation of logic for readability

