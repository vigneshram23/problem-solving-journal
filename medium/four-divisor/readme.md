# Four Divisors (LC 1390)

## 📌 Problem Summary

Given an integer array `nums`, return the sum of divisors of the integers in that array that have **exactly four divisors**.  
If no number in the array has exactly four divisors, return `0`.

### Examples

#### Example 1
```text
Input: nums = [21, 4, 7]
Output: 32

Explanation:
21 → divisors: 1, 3, 7, 21  (4 divisors, sum = 32)
4  → divisors: 1, 2, 4      (3 divisors, ignored)
7  → divisors: 1, 7         (2 divisors, ignored) 
```

## Example 2
```
Input: nums = [21, 21]
Output: 64
(Each 21 contributes 32)
```

## Example 3
```
Input: nums = [1, 2, 3, 4, 5]
Output: 0
(No number has exactly 4 divisors)
```


## 🧠 Core Idea / Approach
A number n has exactly four positive divisors in special cases (like p * q for distinct primes p and q, or p^3 for prime p), but we don’t need explicit prime logic here due to small constraints.
Instead, we use a direct divisor enumeration up to √n:
For each n:
Loop d from 1 to ⌊√n⌋.
If d divides n, we get:
d as one divisor
n / d as the paired divisor
Handle:
d == n/d (perfect square) → count 1 divisor
d != n/d → count 2 divisors
Maintain:
count → number of divisors seen so far
total → sum of divisors
If count ever exceeds 4 → early exit and return 0.
At the end:
If count == 4 → return total
Else → return 0
We also add a simple cache (dict) to store results for repeated numbers (e.g., [21, 21]), avoiding recomputation.

## ⏱ Complexity Analysis
Let M = max(nums) and N = len(nums).
Time Complexity:
Each number takes O(√n) divisor checks.
Overall: O(N * √M)
Given M ≤ 10^5 and N ≤ 10^4, this is efficient.
Space Complexity:
O(1) extra per call, plus O(K) for cache, where K is the number of distinct values in nums.

## ⚠️ Edge Cases
n = 1 → only divisor is 1 → not counted.
Prime numbers (like 2, 3, 5, 7, …) → exactly 2 divisors → ignored.
Perfect squares:
Example: 16 → divisors: 1, 2, 4, 8, 16 (5 divisors) → ignored.
Repeated values:
Example: [21, 21, 21] → we reuse cached result for 21.

## 🌍 Real-World-ish Use Cases
While the problem is mostly mathematical, the pattern of counting limited divisors appears in:
1️⃣ Feature Engineering in ML
Creating numerical features like:
“Number of divisors”
“Has exactly k divisors”
Useful in competition-style tabular problems or anomaly detection on IDs / codes.
2️⃣ Cryptography & Number Theory Tools
Analysis utilities where divisor structure of integers matters.
Pre-filters for special-form integers (e.g., semi-primes, specific divisor counts).
3️⃣ Scoring / Ranking Systems
Game or gamification logic that rewards numbers with special properties
(e.g., scores, IDs, or tokens with exactly four divisors get bonus points).
4️⃣ Educational / Teaching Tools
Interactive number theory demos to show factorization properties and divisor counts.

## 🧪 Example Usage (Local Testing)
from four_divisors import Solution

sol = Solution()
print(sol.sumFourDivisors([21, 4, 7]))   # 32
print(sol.sumFourDivisors([21, 21]))     # 64
print(sol.sumFourDivisors([1, 2, 3, 4])) # 0


