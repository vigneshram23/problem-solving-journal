## 🔍 Problem Overview
Given two integer arrays nums1 and nums2, we need to compute the maximum dot product between non-empty subsequences of the two arrays such that:
Both subsequences have the same length
The relative order of elements is preserved
At least one pair of elements must be selected
🔢 Dot Product Definition
For two sequences A and B of the same length:
dot(A, B) = A[0]*B[0] + A[1]*B[1] + ... + A[k]*B[k]


## 🧠 Key Challenges
Subsequences must be non-empty
Arrays may contain negative values
Maximum result could be negative
Cannot default to 0 (empty subsequence is invalid)

## 💡 Solution Strategy (Dynamic Programming)
We use 2D Dynamic Programming.
DP State
dp[i][j] = maximum dot product using subsequences
           from nums1[i:] and nums2[j:]

DP Transition
At each (i, j), we have three choices:
Take both elements
nums1[i] * nums2[j] + max(0, dp[i+1][j+1])


Skip nums1[i]
dp[i+1][j]


Skip nums2[j]
dp[i][j+1]


We take the maximum of all three.
⚠️ Important Detail
We initialize DP values with negative infinity to guarantee:
At least one element pair is chosen
Negative results are preserved correctly



🧪 Example Test Cases
# Example 1
nums1 = [2,1,-2,5]
nums2 = [3,0,-6]
# Output: 18

# Example 2
nums1 = [3,-2]
nums2 = [2,-6,7]
# Output: 21

# Example 3
nums1 = [-1,-1]
nums2 = [1,1]
# Output: -1


## ⏱️ Complexity Analysis
Metric
Value
Time Complexity
O(n × m)
Space Complexity
O(n × m)
Constraints
Efficient for n, m ≤ 500


## 🌍 Real-World Use Cases
This problem maps directly to several real-world scenarios:
📈 Financial Portfolio Matching
Selecting aligned investment strategies across time while maximizing profit correlation.
🤖 Machine Learning Feature Alignment
Matching feature vectors from two sequences where order matters but elements may be skipped.
🧬 Bioinformatics
Comparing biological sequences (gene/protein scoring) where exact alignment is not required.
🎯 Recommendation Systems
Maximizing relevance scores between user behavior sequences and item sequences.

