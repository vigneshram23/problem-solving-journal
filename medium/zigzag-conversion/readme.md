# Zigzag Conversion

## 📌 Problem Statement
Given a string and a number of rows, write the string in a zigzag
pattern and read it line by line.

---

## 🔍 Example

Input:

s = "PAYPALISHIRING"
numRows = 3

Output:

PAHNAPLSIIGYIR

---

## 🧠 Approach

Instead of building a zigzag matrix, we simulate row traversal:

1. Maintain a list of strings for each row
2. Track current row and direction (up/down)
3. Reverse direction when top or bottom row is reached
4. Append characters row-wise
5. Join all rows to get final result

---

## ⏱ Complexity Analysis

| Metric | Value |
|------|------|
| Time | O(n) |
| Space | O(n) |

---

## ⚠️ Edge Cases Handled

- Single row (`numRows = 1`)
- `numRows` greater than string length
- Short strings
- Mixed character input

---

## 🌍 Real-World Use Cases

### 1️⃣ UI Text Rendering
Used in displaying stylized text layouts or wave animations.

### 2️⃣ Data Encoding
Simple zigzag patterns are used in lightweight obfuscation and encoding schemes.

### 3️⃣ Message Formatting
Rearranging message streams for visualization or logging systems.

### 4️⃣ Interview / Coding Assessments
Tests pattern recognition, traversal logic, and state tracking.

---

## 🚀 Why This Solution Works Well

- Single pass solution
- Easy to understand and debug
- No unnecessary memory usage
- Scales efficiently

---
