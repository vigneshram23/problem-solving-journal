# Smallest Subtree with All the Deepest Nodes

## Problem Statement

Given the root of a binary tree, the depth of each node is defined as the shortest distance to the root.

A node is considered **deepest** if it has the maximum depth among all nodes in the tree.

Your task is to return the **smallest subtree** that contains **all the deepest nodes**.

The subtree of a node consists of that node and all of its descendants.

---

## Examples

### Example 1

Input: [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]

### Example 2

Input: [1]
Output: [1]

### Example 3

Input: [0,1,3,null,2]
Output: [2]

---

## Key Insight

The problem reduces to finding the **Lowest Common Ancestor (LCA)** of all deepest nodes.

Using a **post-order traversal**, we can:
- Compute the maximum depth of each subtree
- Decide which subtree contains all deepest nodes
- Return the smallest subtree root efficiently

---

## Algorithm

For each node:
1. Recursively compute left subtree depth
2. Recursively compute right subtree depth
3. Compare depths:
   - If equal → current node is the answer
   - If left deeper → answer lies in left subtree
   - If right deeper → answer lies in right subtree



## Complexity Analysis
Time Complexity: O(N)
Each node is visited once
Space Complexity: O(H)
Recursive stack where H is the height of the tree

## Real-World Use Cases
1. Distributed Systems & Network Analysis
Finding the lowest common controller handling the deepest leaf services
Identifying the smallest dependency subtree covering all critical nodes
2. File Systems
Finding the lowest directory that contains all deepest files
Useful in permission checks and backup scope optimization
3. Organizational Hierarchies
Finding the smallest team or manager subtree that covers all lowest-level employees
4. Syntax Trees & Compilers
Determining the smallest syntax block containing the deepest expressions
Used in error reporting and scope resolution
5. Knowledge Graphs
Identifying minimal subgraphs that cover all deepest concepts or entities
