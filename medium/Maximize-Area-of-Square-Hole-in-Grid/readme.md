# Maximize Area of Square Hole in Grid

## 🧩 Problem Overview

You are given a grid formed by horizontal and vertical bars.

- The grid contains **n + 2 horizontal** and **m + 2 vertical** bars
- Removing bars merges adjacent 1×1 cells
- You can remove only bars listed in `hBars` and `vBars`
- Your goal is to create the **largest possible square-shaped hole**

---

## 💡 Key Insight

- Removing `k` **consecutive bars** merges `k + 1` unit cells
- A square hole requires equal height and width
- Therefore:
  
square_side = min(max_merged_height, max_merged_width)
area = square_side²


---

## 🧠 Algorithm

1. Sort `hBars` and find the longest consecutive sequence
2. Do the same for `vBars`
3. Convert bar streak length to merged cell count
4. Take the minimum of height and width
5. Return square of that value

---

## 🧪 Example

### Input
```text
n = 2, m = 1
hBars = [2,3]
vBars = [2]
``` 

## Output
4

## Explanation
Horizontal merge: 3 cells
Vertical merge: 2 cells
Square side = 2
Area = 2² = 4

## ⏱ Complexity Analysis
| Metric | Value                  |
| ------ | ---------------------- |
| Time   | `O(H log H + V log V)` |
| Space  | `O(1)` (in-place sort) |


## 🌍 Real-World Applications
- Layout optimization in CAD systems
- Grid-based game mechanics
- Warehouse / floor-plan optimization
- Simulation of removable constraints in 2D space