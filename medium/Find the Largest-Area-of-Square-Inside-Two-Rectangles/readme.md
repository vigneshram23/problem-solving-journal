# 3047. Find the Largest Area of Square Inside Two Rectangles

## 🧩 Problem Statement

You are given `n` axis-aligned rectangles on a 2D plane.  
Each rectangle is represented by:
- `bottomLeft[i] = [ai, bi]`
- `topRight[i] = [ci, di]`

Your task is to find the **maximum area of a square** that can fit inside the
**intersection region of at least two rectangles**.

If no such square exists, return `0`.

---

## 💡 Key Insight

- A square must lie **inside the overlapping region** of two or more rectangles.
- The largest square that fits inside a rectangle is constrained by the **smaller of its width and height**.
- Therefore:
  1. Check **every pair of rectangles**
  2. Compute their intersection
  3. From that intersection, compute the largest square possible

---

## 🧠 Algorithm

1. Iterate over all pairs of rectangles `(i, j)`
2. Compute intersection:
   - `x_left = max(x1_i, x1_j)`
   - `y_bottom = max(y1_i, y1_j)`
   - `x_right = min(x2_i, x2_j)`
   - `y_top = min(y2_i, y2_j)`
3. Compute:
   - `width = x_right - x_left`
   - `height = y_top - y_bottom`
4. If both are positive:
   - `square_side = min(width, height)`
   - Update maximum area

---

## ✅ Example

### Input
```text
bottomLeft = [[1,1],[1,3],[1,5]]
topRight  = [[5,5],[5,7],[5,9]]

Output
4
```

## Explanation
Intersection height = 2
Intersection width = 4
Largest square side = 2 → area = 4

## ⏱ Complexity Analysis
| Metric           | Value   |
| ---------------- | ------- |
| Time Complexity  | `O(n²)` |
| Space Complexity | `O(1)`  |

With n ≤ 1000, this solution runs efficiently within constraints.

## 🌍 Real-World Use Cases
Computer Graphics: Finding maximum square crop inside overlapping regions
Geospatial Systems: Identifying maximal usable square land area
Game Engines: Collision-based region analysis
CAD / Design Tools: Optimal placement within overlapping layouts

## 🏁 Conclusion
This solution efficiently checks all possible intersections and guarantees
the maximum square area inside at least two rectangles using a clean and
intuitive geometric approach.