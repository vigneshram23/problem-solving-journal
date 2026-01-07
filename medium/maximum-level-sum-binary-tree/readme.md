# Maximum Level Sum of a Binary Tree

**LeetCode Problem:** 1161  
**Difficulty:** Medium  
**Topic:** Binary Tree, Breadth-First Search (BFS)

---

## 📌 Problem Statement

Given the root of a binary tree:

- The root is at **level 1**
- Its children are at **level 2**
- And so on…

Return the **smallest level number** such that the **sum of node values at that level is maximum**.

---

## 🧠 Approach

We solve this problem using **Level Order Traversal (Breadth-First Search)**.

### Key Ideas
- Traverse the tree **level by level**
- Compute the **sum of node values at each level**
- Track:
  - Maximum sum seen so far
  - The smallest level that achieved this sum
- Update result **only when the new sum is strictly greater**  
  (ensures smallest level is returned in case of ties)

---

## 🧮 Algorithm Steps

1. Initialize a queue with the root node
2. Start level counter from `1`
3. While the queue is not empty:
   - Process all nodes at the current level
   - Calculate their sum
   - Add child nodes to the queue
4. Update the result if current level sum is greater than the maximum
5. Return the stored level number

---

## ⏱️ Time & Space Complexity

| Metric | Complexity |
|------|------------|
| **Time Complexity** | `O(n)` |
| **Space Complexity** | `O(w)` |

Where:
- `n` = total number of nodes
- `w` = maximum width of the tree (nodes at the widest level)

---

## ✅ Example

Input:
```text
[1, 7, 0, 7, -8, null, null]

Level-wise sums:
Level 1 → 1
Level 2 → 7
Level 3 → -1
Output:
2
``` 


## 🌍 Real-World Applications
This pattern appears in many real systems:
1️⃣ Organizational Hierarchies
Finding the team level with maximum combined performance score
2️⃣ Network Traffic Analysis
Identifying the most active layer in a network topology
3️⃣ File System Structures
Finding directory depth with maximum file size usage
4️⃣ Game Trees & AI
Evaluating which depth of a decision tree produces the strongest outcome

## 🛠️ Technologies Used
Python
Deque (collections)
Binary Tree Traversal
