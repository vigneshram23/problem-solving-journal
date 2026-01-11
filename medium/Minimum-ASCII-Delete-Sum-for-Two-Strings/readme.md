##  Key Idea
This problem is a dynamic programming variant of Longest Common Subsequence (LCS).
Instead of:
maximizing the length of the common subsequence,
we are:
minimizing the ASCII cost of deletions needed to make both strings equal.

##  Approach
DP Definition
Let:
dp[i][j] = minimum ASCII delete sum 
           to make s1[i:] and s2[j:] equal

## Transition Rules
If characters match
s1[i] == s2[j]
dp[i][j] = dp[i+1][j+1]


If characters do not match
dp[i][j] = min(
    ord(s1[i]) + dp[i+1][j],   # delete from s1
    ord(s2[j]) + dp[i][j+1]    # delete from s2
)


Base Cases
If one string is exhausted, delete all remaining characters from the other string.


## ⏱ Complexity Analysis
Metric
Complexity
Time
O(m × n)
Space
O(n)
Input Constraints
Handles up to 1000 × 1000


## 🧩 Real-World Use Cases
1. Text Synchronization Systems
Used in diff/merge tools where deletions have weighted costs.
2. Version Control Optimization
Minimizing change costs between file versions.
3. Data Cleaning Pipelines
Aligning noisy text records with minimal loss.
4. Natural Language Processing
Computing similarity with weighted edit operations.
5. DNA / Bioinformatics Alignment
Character-level alignment where deletion penalties vary.

## 🧠 Interview Takeaways
This is not edit distance (no insert/replace)
Think LCS + cost
Strong example of:
Optimal substructure
Space optimization
Bottom-up DP

