# LeetCode 3650 – Minimum Cost Path with Edge Reversals

## 🧩 Problem Summary

You are given a **directed weighted graph** with `n` nodes.

Each node has a **switch** that can be used **at most once**:
- When you arrive at a node, you may reverse **one incoming edge**
- The reversed edge can be used immediately at **double cost**
- Goal: find the **minimum cost** to travel from node `0` to node `n-1`

---

## 💡 Key Insight

Although each node has a switch usable only once, **we do not need to track switch usage explicitly**.

Why?
- Switch usage is **local to the node**
- Reusing a switch at the same node would always increase cost
- Dijkstra naturally avoids suboptimal revisits

So the problem reduces to:
> Treat every edge as usable in both directions, with reversed direction costing `2 × weight`

---

## 🔁 Graph Transformation

For each original edge:
u → v (cost w)
We add:
- Normal edge:  

u → v (cost w)
- Reversed edge (via switch at v):  

v → u (cost 2w)

---

## 🚀 Algorithm
1. Build adjacency list with normal + reversed edges
2. Run **Dijkstra’s algorithm** from node `0`
3. Return distance to node `n-1`
---

## ✅ Example
### Input
n = 3
edges = [[2,1,1],[1,0,1],[2,0,16]]


### Optimal Path
0 → 1 (reverse 1→0, cost 2)
1 → 2 (reverse 2→1, cost 2)
Total = 4


---

## 🧪 Complexity Analysis

- **Time Complexity:** `O((n + m) log n)`
- **Space Complexity:** `O(n + m)`

Where:
- `n` = number of nodes
- `m` = number of edges

---

## 🧠 Interview Takeaway

> Some constraints exist only to guide modeling — not to add state.  
> Recognizing when Dijkstra alone is sufficient is a key graph insight.

---



