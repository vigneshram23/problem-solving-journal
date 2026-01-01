# 🧠 Problem: Least Recently Used (LRU) Cache

## 📌 Level
**Easy**

## 🧩 Problem Statement
Design and implement a **Least Recently Used (LRU) Cache** that supports the following operations in **O(1)** time:

- `get(key)`: Return the value if the key exists, otherwise return `-1`.
- `put(key, value)`: Insert or update the value. If the cache exceeds capacity, evict the **least recently used** item.

---

## 🧪 Example

```python
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)       # returns 1
cache.put(3, 3)    # evicts key 2
cache.get(2)       # returns -1 (not found)
```  

## 🧵 Implementations
### 1️⃣ Basic Version (LRUCacheBasic)

A simple Python implementation using:
- dict to store key-value pairs
- list to track usage order
⚠️ Limitation: list.remove() and list.pop(0) are O(n), so it's not truly O(1).

## 2️⃣ Optimized Version (LRUCache)

A production-ready version using Python’s built-in OrderedDict:
- Maintains insertion order
- Allows moving keys to end (mark as recently used)
- Efficient O(1) get() and put() operations
✅ This is the recommended version for interviews and real systems.

## ⚙️ Time & Space Complexity
| Operation | Basic Version | Optimized Version |
| --------- | ------------- | ----------------- |
| `get()`   | O(n)          | O(1)              |
| `put()`   | O(n)          | O(1)              |
| Space     | O(capacity)   | O(capacity)       |

## 🌐 Real-World Use Cases
- Web Browsers: Store most recently visited pages.
- Content Delivery Networks (CDNs): Cache frequently accessed assets.
- Database Systems: Page replacement algorithms.
- Operating Systems: Disk and memory caching.

## 💡 Learning Outcome
This exercise demonstrates:
- How to maintain order in cache eviction logic.
- Differences between naive and optimized implementations.
- Why data structures (like OrderedDict) matter for performance.