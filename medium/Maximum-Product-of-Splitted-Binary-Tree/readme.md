# LeetCode 1339 — Maximum Product of Splitted Binary Tree

## Problem
Given the root of a binary tree, remove exactly one edge to split the tree into two subtrees.  
Let the sums of the two subtrees be `S1` and `S2`.  
Return the **maximum possible product** `S1 * S2`, and return the result modulo `1e9 + 7`.

**Important:** You must maximize the product **before** applying modulo.

---

## Key Insight
If the total sum of the entire tree is `T`, and a chosen subtree has sum `S`, then cutting the edge above that subtree creates:
- subtree sum: `S`
- remaining tree sum: `T - S`

So the product for that cut is:
`S * (T - S)`

Therefore, we just need:
1. Total sum `T`
2. All subtree sums `S`
3. Maximize `S * (T - S)` over all nodes

---

## Approach (Iterative, Production-Safe)
We use two passes:

### Pass 1: Compute Total Sum
Iterative DFS to compute `T`.

### Pass 2: Compute Subtree Sums + Max Product
Iterative **postorder traversal** to compute subtree sums bottom-up.
For each subtree sum `S`, compute product `S * (T - S)` and track the maximum.

This avoids recursion depth issues for trees with up to 50,000 nodes.

---

## Complexity
- **Time:** `O(N)` — each node processed a constant number of times
- **Space:** `O(N)` — stores subtree sums, plus traversal stack

---

## Real-World Use Case (Practical Analogy)
Imagine a company has a hierarchical org structure (a tree):
- each node = department/team
- node value = annual budget/revenue contribution

You want to split the org into two independent business units by removing one reporting line (one edge),
such that the product of the total contributions of the two new units is maximized — i.e., you want a split
that produces two strong, balanced business units.

This same pattern applies to:
- splitting compute clusters or service trees into two balanced groups
- partitioning a dependency tree into two high-value components
- dividing a portfolio hierarchy into two high-impact segments

---

## Implementation Notes
- We maximize the raw integer product first, then apply modulo at the end.
- We use iterative traversals to avoid recursion-limit crashes on skewed trees.

---

## Example
Input: `[1,2,3,4,5,6]`  
Total sum = 21  
Best split produces sums 11 and 10 → product = 110

---

## Code
See `solution.py` (or the code section in the submission).
