# Median of Two Sorted Arrays

## 📌 Problem Statement
Given two sorted arrays `nums1` and `nums2` of sizes `m` and `n`,
return the median of the two sorted arrays.

**Constraint:**  
The overall runtime complexity must be **O(log (m + n))**.

---

## 🔍 Example

### Example 1
**Input**
nums1 = [1, 3]
nums2 = [2]


**Output**
2.0


---

### Example 2
**Input**
nums1 = [1, 2]
nums2 = [3, 4]


**Output**
2.5


---

## 🧠 Optimal Approach (Binary Search Partitioning)

Instead of merging arrays (which is inefficient), we:

1. Perform **binary search on the smaller array**
2. Partition both arrays such that:

max(left_part) <= min(right_part)

3. Once the correct partition is found:
- If total length is even → average of two middle values
- If odd → max of left partitions

This ensures optimal performance.

---

## ⏱ Complexity Analysis

| Metric | Value |
|------|------|
| Time Complexity | **O(log(min(m, n)))** |
| Space Complexity | **O(1)** |

---

## ⚠️ Edge Cases Handled

- One array empty
- Arrays of different sizes
- Negative values
- Even and odd total lengths
- Single-element arrays

---

## 🌍 Real-World Use Cases

### 1️⃣ Financial Analytics
Finding the median transaction value across two sorted datasets
(e.g., online vs offline transactions).

### 2️⃣ Healthcare Systems
Combining patient vitals from two departments to compute median values
(e.g., blood pressure readings).

### 3️⃣ Distributed Systems
Aggregating latency metrics from two sorted sources (microservices).

### 4️⃣ Recommendation Systems
Finding median user ratings from multiple sorted streams.

### 5️⃣ Data Engineering Pipelines
Efficient aggregation of sorted data partitions without full merge.

---

## 🧪 How to Run

```bash
python median_of_two_sorted_arrays.py
