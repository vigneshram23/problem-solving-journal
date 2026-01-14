# 3453. Separate Squares I

**Topic:** Sweep Line, Geometry, Prefix Area  
**Language:** Python  

---

## 🧩 Problem Summary

You are given multiple axis-aligned squares. Each square is defined by:
- Bottom-left corner `(x, y)`
- Side length `l`

Your task is to find the **minimum y-coordinate** of a horizontal line such that:

> The total area of squares **above** the line equals the total area **below** the line.

### Important Notes
- Squares may **overlap**
- Overlapping areas are counted **multiple times**
- Answers within `1e-5` of the true value are accepted

---

## 💡 Key Insight

Instead of performing binary search over the y-axis and recomputing areas repeatedly, we can:

- Convert each square into **vertical sweep events**
- Maintain a running **area accumulation rate**
- Integrate area continuously while sweeping upward

This reduces repeated computations and significantly improves performance.

---

## 🚀 Approach: Sweep Line with Prefix Area Integration

### Event Representation
For a square starting at `y` with side `l`:
- `(y, +l)` → square starts contributing area
- `(y + l, -l)` → square stops contributing area

### During the Sweep
- `curr_rate` represents the total active horizontal width
- Area accumulated between two y-values is:
  

area = curr_rate × height

When cumulative area reaches half of the total area, the exact y-coordinate is computed analytically.

---

## 🧠 Algorithm Steps

1. Convert all squares into sweep events
2. Sort events by y-coordinate
3. Sweep bottom to top, accumulating area
4. Stop once half of the total area is reached
5. Compute the exact y-coordinate mathematically

---

## ⏱ Time & Space Complexity

| Metric | Complexity |
|------|------------|
| Time | `O(N log N)` |
| Space | `O(N)` |

Where `N` is the number of squares.

---

## ✅ Why This Works Well

- Avoids repeated scans of all squares
- Uses continuous integration instead of binary search
- Handles overlapping squares naturally
- Efficient enough for large inputs (`N ≤ 50,000`)

---

## 🧪 Example

**Input**

[[0,0,2],[1,1,1]]

**Output**

1.16667

---

## 📌 Takeaway

This problem is an excellent example of replacing brute-force numeric search with a **geometric sweep-line technique**, resulting in dramatic performance improvements.
