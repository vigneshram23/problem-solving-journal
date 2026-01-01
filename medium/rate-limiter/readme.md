# 🚦 Problem: Rate Limiter using Sliding Window Log

## 📌 Level
**Medium**

---

## 🧩 Problem Statement

Design a **rate limiter** that allows a maximum number of requests per user within a fixed time window, using the **sliding window log algorithm**.

---

## ✅ Requirements

- `allow_request(user_id)` → Returns `True` if the request is allowed, `False` otherwise.
- Supports:
  - Configurable max requests and time window.
  - Concurrency safety.
  - Memory cleanup for old request logs.

---

## 🧪 Example

```python
limiter = RateLimiter(max_requests=3, window_seconds=60)

print(limiter.allow_request("user1"))  # True
print(limiter.allow_request("user1"))  # True
print(limiter.allow_request("user1"))  # True
print(limiter.allow_request("user1"))  # False (limit exceeded)
``` 

## ⚙️ Implementation Overview
This solution:
- Uses a sliding window log algorithm.
- Stores a list of timestamps per user.
- Cleans up outdated entries before evaluating request allowance.
- Uses threading.Lock to ensure thread safety.    

## 🔍 Time & Space Complexity
| Operation         | Time Complexity | Space Complexity              |
| ----------------- | --------------- | ----------------------------- |
| `allow_request()` | O(n) per user   | O(n * u) → timestamps * users |
| `cleanup_user()`  | O(1)            | Reduces per-user storage      |


## 📊 Comparison of Rate Limiting Algorithms
| Algorithm              | Description          | Memory | Accuracy | Use Case               |
| ---------------------- | -------------------- | ------ | -------- | ---------------------- |
| Fixed Window           | Bucketed by time     | Low    | Low      | Simple APIs            |
| **Sliding Window Log** | Logs all timestamps  | High   | High     | Real-time protection   |
| Sliding Window Counter | Partial buckets      | Medium | Medium   | Balanced performance   |
| Token/Leaky Bucket     | Token-based queueing | Varies | High     | Streaming, bursty APIs |


## 🌐 Real-World Use Cases
- 🛡️ API Rate Limiting – Prevent abuse and DoS attacks
- 🔐 Login Throttling – Stop brute force attempts
- 📲 Messaging Apps – Avoid user spam
- 🔁 E-Commerce Systems – Limit inventory-check frequency

## ⚠️ Limitations
- Memory usage can grow large if many users make frequent requests and their logs are not cleaned up.
- For production systems with very high scale, Sliding Window Counter or Token Bucket might be more optimal.

## 🧠 Learning Outcome
By solving this, I learned:
- How rate limiting protects systems from abuse.
- Different rate limiting strategies and their trade-offs.
- Importance of concurrency control in real-world backend systems.
- Using defaultdict and Lock for safe shared state in Python.