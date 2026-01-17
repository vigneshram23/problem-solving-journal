# LeetCode 2975 – Maximum Square Area by Removing Fences From a Field

## 🧠 Problem Summary
You are given a large rectangular field with fixed boundary fences and some removable internal fences.
By removing some internal fences, you need to determine the **maximum possible square area** that can be formed.

If forming a square is impossible, return `-1`.

---

## 🔍 Key Insight
A square can be formed **only if**:
- The distance between two horizontal fences equals
- The distance between two vertical fences

Since internal fences can be removed, the problem reduces to:
> Find the **largest common distance** between any two horizontal fences and any two vertical fences.

---

## 🛠️ Approach
1. Add **boundary fences** (`1` and `m`, `1` and `n`) to ensure all possible segments are considered.
2. Compute **all pairwise distances** between horizontal fences.
3. Compute **all pairwise distances** between vertical fences.
4. Find the **maximum distance common to both sets**.
5. Return the square of that distance modulo `10⁹ + 7`.

---

## ✅ Example

### Input
m = 4, n = 3
hFences = [2, 3]
vFences = [2]


### Output
4


### Explanation
Removing the fences at `2` allows a square of side `2`, giving area `2 × 2 = 4`.

---

## ⏱️ Complexity Analysis
- **Time Complexity:**  
  `O(H² + V²)`  
  where `H = len(hFences) + 2` and `V = len(vFences) + 2`

- **Space Complexity:**  
  `O(H²)` for storing horizontal distances

This is efficient because `H, V ≤ 602`.

---

## 🌍 Real-World Analogy
Imagine a large farmland divided by removable fences.
You want to allocate the **largest possible square plot** for construction by removing unnecessary internal fences.
This solution finds the optimal square size efficiently.

---
