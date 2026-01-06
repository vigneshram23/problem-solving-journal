# Maximum Matrix Sum (LeetCode 1975)

## 📌 Problem Overview

You are given an `n x n` integer matrix.  
You can perform the following operation any number of times:

- Select **two adjacent elements** (sharing a border)
- Multiply **both elements by `-1`**

The goal is to **maximize the sum of all elements in the matrix**.

---

## 🧠 Key Insight

The operation allows redistribution of negative signs across the matrix.

### Critical observations:
- If the number of negative values is **even**, all values can be made positive.
- If the number of negative values is **odd**, **one value must remain negative**.
- To minimize loss, that value should be the **smallest absolute value** in the matrix.

---

## ✅ Strategy

1. Compute the **sum of absolute values** of all elements.
2. Count how many elements are **negative**.
3. Track the **minimum absolute value**.
4. If the negative count is odd, subtract `2 × min_absolute_value`.

---

## 🧮 Algorithm


total_sum = sum(abs(all elements))
negative_count = count of negative elements
min_abs = minimum absolute value
if negative_count is odd:
total_sum -= 2 * min_abs

---

## ⏱ Time & Space Complexity

| Metric | Value |
|------|------|
Time Complexity | **O(n²)**
Space Complexity | **O(1)**

Efficient enough for `n ≤ 250`.

---

## 🧪 Example

### Input

matrix = [
[1, 2, 3],
[-1, -2, -3],
[1, 2, 3]
]

### Output

16

### Explanation
One negative value (with smallest magnitude) must remain negative.

---

## 🏭 Real-World Analogy

This problem is analogous to:

- **Financial portfolio optimization**: minimizing loss when complete profit is impossible
- **Signal processing**: phase inversion with parity constraints
- **Manufacturing systems**: optimizing yield under unavoidable defects

---

## 🧪 Testing

The implementation includes built-in sanity tests:

```python
assert solution.maxMatrixSum([[1, -1], [-1, 1]]) == 4
assert solution.maxMatrixSum([[1, 2, 3], [-1, -2, -3], [1, 2, 3]]) == 16
assert solution.maxMatrixSum([[-1, 0], [2, 3]]) == 6
```

