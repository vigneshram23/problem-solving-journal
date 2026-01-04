# Longest Palindromic Substring

**Difficulty:** Medium  
**Problem ID:** LeetCode #5  

---

## 📌 Problem Statement

Given a string `s`, return the **longest palindromic substring** in `s`.

A palindrome is a string that reads the same forward and backward.

---

## 🧠 Approach: Expand Around Center

A palindrome expands symmetrically from its center.

There are **two possible palindrome centers**:
1. **Odd-length palindrome** (e.g., `"aba"`)
2. **Even-length palindrome** (e.g., `"bb"`)

For each index in the string:
- Expand left and right for odd-length palindromes
- Expand left and right for even-length palindromes
- Track the longest valid palindrome found

---

## 🧪 Example

### Input
```text
s = "babad"

Output
"bab"

("aba" is also a valid answer)
``` 


## ⏱️ Time & Space Complexity
| Metric | Complexity |
| ------ | ---------- |
| Time   | **O(n²)**  |
| Space  | **O(1)**   |

This is optimal for the given constraint: 1 ≤ s.length ≤ 1000


## 🚀 Real-World Use Cases
1. Text Processing & NLP
Detecting symmetric patterns in strings
Linguistic analysis of words or phrases

2. DNA / Genome Sequencing
Identifying palindromic DNA sequences
Useful in bioinformatics and genetics research

3. Data Validation
Pattern matching for validation rules
Detecting mirrored or symmetric identifiers

4. Search & Autocomplete Systems
Highlighting palindromic phrases
Intelligent text analytics