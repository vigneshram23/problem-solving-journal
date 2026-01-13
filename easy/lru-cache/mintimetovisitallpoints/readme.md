# 1266. Minimum Time Visiting All Points

## 🧠 Problem Summary

You are given a list of points on a 2D plane.  
Starting from the first point, you must visit **all points in order**.

### Allowed movements (per second):
- Move **1 unit horizontally**
- Move **1 unit vertically**
- Move **diagonally** (1 unit x + 1 unit y)

Your task is to calculate the **minimum time in seconds** required to visit all points.

---

## 💡 Key Insight

To move from point **A(x₁, y₁)** to **B(x₂, y₂)**:

- Let  

dx = |x₂ - x₁|
dy = |y₂ - y₁|
- Each diagonal move reduces both `dx` and `dy` by 1
- Optimal strategy:
- Take `min(dx, dy)` diagonal moves
- Then finish remaining straight moves

👉 **Minimum time between two points = max(dx, dy)**

---

## ✅ Algorithm

1. Iterate through consecutive point pairs
2. For each pair:
 - Compute `dx` and `dy`
 - Add `max(dx, dy)` to total time
3. Return accumulated time

---

## 🧪 Example

**Input**

points = [[1,1],[3,4],[-1,0]]

**Steps**
- (1,1) → (3,4) = max(2,3) = 3
- (3,4) → (-1,0) = max(4,4) = 4

**Output**

7

---
## ⏱️ Complexity Analysis
Time Complexity: O(n)
Space Complexity: O(1)
Where n is the number of points.

## 🌍 Real-World Applications
Robot navigation on grid-based maps
Game AI movement optimization
Path planning in simulations
Logistics routing on discrete coordinate systems
