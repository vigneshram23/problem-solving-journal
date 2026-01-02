# Longest Substring Without Repeating Characters

**LeetCode Problem #3**  
**Difficulty:** Medium  
**Category:** Sliding Window, Hash Set  

---

## 📌 Problem Statement

Given a string `s`, find the length of the **longest substring**
that contains **no repeating characters**.

> A substring must be **contiguous**.
> A subsequence is **not allowed**.

---

## 🧪 Examples

### Example 1
**Input:**  
s = "abcabcbb"

**Output:**  
**Explanation:**  
The longest substring without repeating characters is `"abc"`.

---

### Example 2
**Input:**  
s = "bbbbb"

**Output:**  
1

**Explanation:**  
The longest substring is `"b"`.

---

### Example 3
**Input:**  
s = "pwwkew"

**Output:**  
3

**Explanation:**  
The answer is `"wke"`.  
`"pwke"` is a subsequence, not a substring.

---

## 🧠 Approach

### Sliding Window Technique

- Use two pointers (`left`, `right`) to represent a window
- Use a **set** to track characters in the current window
- Expand the window when characters are unique
- Shrink the window when a duplicate is found
- Track the maximum window size

---

## 🧮 Complexity Analysis

| Metric | Value |
|------|------|
| Time Complexity | **O(n)** |
| Space Complexity | **O(min(n, charset))** |

---

## 🧩 Python Implementation

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen_chars = set()
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            while char in seen_chars:
                seen_chars.remove(s[left])
                left += 1

            seen_chars.add(char)
            max_length = max(max_length, right - left + 1)

        return max_length
```

## ✅ Key Takeaways
- Sliding Window avoids unnecessary re-computation
- Hash Set enables constant-time lookups
- Clean window maintenance ensures linear performance
- This is a frequently asked interview problem


## 🌍 Real-World Applications
This problem isn't just a coding puzzle — it's directly useful in several real-world systems:
✅ 1. Text Editors & IDEs
 Features like syntax highlighting, auto-completion, and search tools may need to analyze substrings without duplicates (e.g., unique variable or keyword suggestions).

✅ 2. Streaming Platforms
 While scanning logs, playlists, or search histories, systems may look for longest non-repeating sessions or user actions to detect natural content segmentation or recommendation intervals.

✅ 3. Cybersecurity & Authentication
 To detect non-repeating character patterns in passwords or input sequences to ensure complexity and avoid repetition-based vulnerabilities.

✅ 4. Natural Language Processing (NLP)
 Used in token analysis, spell checkers, or compression algorithms where repeated patterns must be identified and optimized.

✅ 5. Web Browsers / URL Parsers
 Parsing URLs, cookies, or session tokens often involves tracking unique sequences (e.g., longest sequence of distinct path parameters).
