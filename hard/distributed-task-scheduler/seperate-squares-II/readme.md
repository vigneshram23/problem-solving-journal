# Separate Squares II – LeetCode 3454 (Hard)

## Problem Summary
You are given multiple axis-aligned squares on a 2D plane.  
Squares may **overlap**, and overlapping regions must be counted **only once**.

Your task is to find the **minimum y-coordinate** of a horizontal line such that:
- Union area **above** the line equals
- Union area **below** the line

Precision within **1e-5** is acceptable.

---

## Key Challenges
- Overlapping squares (union area, not sum of areas)
- Very large coordinate limits (`up to 10^9`)
- Efficient handling for up to `50,000` squares

---

## Solution Approach

### 1. Sweep Line on Y-axis
Each square `[x, y, l]` contributes:
- Start event at `y`
- End event at `y + l`
- Active x-interval `[x, x + l]`

---

### 2. Union of Intervals
At any horizontal slice:
- Compute the **union length** of active x-intervals
- Multiply by vertical height to get area

This avoids double-counting overlaps.

---

### 3. Two-Pass Strategy
**Pass 1:** Compute total union area  
**Pass 2:** Sweep again and stop when cumulative area ≥ half

Interpolation gives the exact y-coordinate.

---

## Time & Space Complexity
- **Time:** `O(N log N)`
- **Space:** `O(N)`

Where `N` is the number of squares.

---

## Real-World Use Cases

- **Geospatial analytics**  
  Splitting land or coverage area equally.

- **Computer graphics & rendering**  
  Balanced partitioning of overlapping layers.

- **Urban planning & simulation**  
  Equal-area zoning problems.

- **Physics simulations**  
  Mass or density-based vertical partitioning.

---

## Example

### Input
```python
squares = [[0, 0, 2], [1, 1, 1]]

1.00000
``` 