## Construct the Minimum Bitwise Array I

## 🧩 Problem Statement
You are given an array `nums` consisting of `n` prime integers.
Construct an array `ans` such that for every index `i`:
ans[i] OR (ans[i] + 1) == nums[i]

Additionally:
- Each `ans[i]` must be **as small as possible**
- If it is not possible, set `ans[i] = -1`

---

## 💡 Key Observations

### 1. Even Numbers Are Impossible
For any integer `x`:
- `x` and `x + 1` always differ in the least significant bit
- Their bitwise OR is **always odd**
➡️ If `nums[i]` is even, **no solution exists**
---

### 2. Odd Numbers Always Have a Solution
For odd numbers, the result depends on the number of **trailing 1s** in the binary representation.
Example:
7 = 111 (trailing ones = 3)
3 = 011
3 OR 4 = 7
---

## 🧠 Core Idea
For an odd number `n`:
- Let `t` = number of trailing `1`s in binary representation of `n`
- The **minimum** valid value is:

ans = n - 2^(t - 1)

Trailing ones can be computed efficiently using:
n ^ (n + 1)
---

## 🛠 Algorithm

For each number `n` in `nums`:
1. If `n` is even → append `-1`
2. Else:
   - Compute `xor = n ^ (n + 1)`
   - Count trailing ones: `t = bit_length(xor) - 1`
   - Append `n - 2^(t - 1)`

---

## 🧪 Examples
### Example 1
**Input**
nums = [2,3,5,7]

**Output**
[-1,1,4,3]
---

### Example 2
**Input**
nums = [11,13,31]

**Output**
[9,12,15]



## ⏱ Complexity Analysis
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)` (excluding output array)
---

## ✅ Takeaways
- Bitwise OR with consecutive numbers always produces an odd number
- Trailing 1s play a critical role in minimizing the result
- Efficient bit manipulation avoids brute force

---
