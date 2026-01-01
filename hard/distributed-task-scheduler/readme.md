# 🧠 Problem: Distributed Task Scheduler

## 📌 Level
**Hard**

---

## 🧩 Problem Statement

Design a **task scheduler** that supports:

- ✅ Task dependencies
- ✅ Task priorities (lower number = higher priority)
- ✅ Parallel execution
- ✅ Detection of circular dependencies

Each task should only run when its dependencies are satisfied, and tasks without dependencies can run in parallel (up to `max_workers`).

---

## ✅ Requirements

- `add_task(task_id, priority, dependencies, execution_func)`
- `execute()` → Returns task statuses & results
- Parallel execution using `ThreadPoolExecutor`
- Safe from circular dependency deadlocks

---

## 🧪 Example

```python
scheduler = TaskScheduler(max_workers=2)

scheduler.add_task("A", 1, [], lambda: "A done")
scheduler.add_task("B", 2, ["A"], lambda: "B done")
scheduler.add_task("C", 1, ["A"], lambda: "C done")
scheduler.add_task("D", 3, ["B", "C"], lambda: "D done")

results = scheduler.execute()
print(results)
```

### Expected execution order:
* A runs first.
* B and C run in parallel (after A).
* D runs after B and C.

## ⚙️ Implementation Overview
- ✅ Uses DFS to detect circular dependencies.
- ✅ Uses ThreadPoolExecutor for concurrency.
- ✅ Tracks task statuses (pending, running, completed, failed).
- ✅ Results returned as a dictionary {task_id: {status/result/error}}.

## 🔍 Time & Space Complexity
| Operation       | Time Complexity                  | Space Complexity               |
| --------------- | -------------------------------- | ------------------------------ |
| Cycle detection | O(V + E) (DFS traversal)         | O(V) for visited + recursion   |
| Execution loop  | O(N) (task submission + polling) | O(N) for future/result storage |

#### N = number of tasks, V = nodes, E = edges in dependency graph 

## 🌐 Real-World Use Cases
- ⚙️ Airflow-like DAG scheduling
- 🧪 ML Pipelines (e.g., preprocess → train → evaluate)
- 🔁 CI/CD Job Scheduling (e.g., Jenkins pipeline)
- 🔗 ETL Workflows
- 🚀 Distributed Computing Task Graphs

## ⚠️ Limitations
| Limitation             | Notes                           |
| ---------------------- | ------------------------------- |
| ❌ No retry logic       | Can be added in future versions |
| ❌ No timeouts per task | Not yet supported               |
| ❌ No visual DAG export | Currently text-based only       |


## 🧠 Learning Outcome
This problem helped me:
- Apply graph traversal (DFS) to real-world systems.
- Understand concurrent execution with dependencies.
- Think in terms of dependency resolution and topological order.
- Build a parallel scheduler from scratch with failure handling.