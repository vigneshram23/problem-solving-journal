# Maximal Rectangle (LeetCode 85)

## 📌 Problem Statement

Given a binary matrix filled with `'0'`s and `'1'`s, find the area of the
largest rectangle containing only `'1'`s.

### Example


Input:
[
["1","0","1","0","0"],
["1","0","1","1","1"],
["1","1","1","1","1"],
["1","0","0","1","0"]
]
Output:
6

---

## 💡 Key Insight

A rectangle of `1`s must:
- Span **consecutive rows**
- Cover **contiguous columns**

Instead of checking every rectangle (which is inefficient), we:
1. Treat **each row as the base of a histogram**
2. Convert the 2D problem into **multiple 1D histogram problems**
3. Solve each histogram using a **monotonic stack**

This leverages the classic **Largest Rectangle in Histogram** technique.

---

## 🧠 Algorithm Explanation

### Step 1: Build Histogram Heights
For each column:
- If the cell is `'1'`, increment height
- If the cell is `'0'`, reset height to `0`

This converts each row into a histogram of heights.

### Step 2: Largest Rectangle in Histogram
- Maintain a stack of indices with increasing heights
- When a smaller height appears:
  - Pop from stack
  - Compute area using:
    ```
    area = height * width
    ```
- Append a sentinel `0` to flush remaining stack elements

---

## 🧪 Example Walkthrough

For row:

["1","1","1","1","1"]

Histogram heights might be:

[3, 1, 3, 2, 2]

Largest rectangle computed using stack logic gives area `6`.

---

## ⏱️ Complexity Analysis

| Metric | Value |
|------|------|
| Time Complexity | `O(rows × cols)` |
| Space Complexity | `O(cols)` |

Each column index is pushed and popped **at most once per row**.

---

## 🧩 Why This Solution is Optimal

- Avoids brute force rectangle checks
- Efficient stack-based computation
- Scales well up to `200 x 200` matrix limits
- Commonly expected in **senior-level interviews**

---

## 🌍 Real-World Applications

- Image processing (binary image segmentation)
- Heatmap and grid analytics
- Document layout analysis
- Video frame pattern detection
- Binary feature extraction in ML pipelines

---

## 🚀 How to Run

```python
matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]

print(Solution().maximalRectangle(matrix))  # Output: 6
```