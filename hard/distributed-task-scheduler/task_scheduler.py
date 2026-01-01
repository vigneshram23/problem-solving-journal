"""
Task Scheduler - Hard Level Problem
-----------------------------------
Design a scheduler that:
- Handles task dependencies and priority-based execution.
- Executes tasks in parallel where possible.
- Detects and prevents circular dependencies.
"""

from concurrent.futures import ThreadPoolExecutor
from typing import Callable, List, Dict, Any, Set
from threading import Lock
import time


class TaskScheduler:
    def __init__(self, max_workers: int = 4):
        """
        Initialize the scheduler with a thread pool.

        :param max_workers: Max number of parallel worker threads.
        """
        self.max_workers = max_workers
        self.tasks = {}  # task_id -> task info
        self.lock = Lock()

    def add_task(
        self,
        task_id: str,
        priority: int,
        dependencies: List[str],
        execution_func: Callable[[], Any]
    ) -> None:
        """
        Add a task to the scheduler.

        :param task_id: Unique task identifier.
        :param priority: Execution priority (lower = higher priority).
        :param dependencies: List of task_ids this task depends on.
        :param execution_func: The function to execute.
        """
        with self.lock:
            self.tasks[task_id] = {
                "priority": priority,
                "dependencies": set(dependencies),
                "func": execution_func,
                "status": "pending",
                "result": None,
            }

    def _detect_circular_dependencies(self) -> bool:
        """
        Detect circular dependencies using DFS.

        :return: True if cycle is found, else False.
        """
        visited = set()
        rec_stack = set()

        def has_cycle(task_id: str) -> bool:
            visited.add(task_id)
            rec_stack.add(task_id)

            for dep in self.tasks[task_id]["dependencies"]:
                if dep not in visited:
                    if has_cycle(dep):
                        return True
                elif dep in rec_stack:
                    return True

            rec_stack.remove(task_id)
            return False

        for task_id in self.tasks:
            if task_id not in visited:
                if has_cycle(task_id):
                    return True
        return False

    def execute(self) -> Dict[str, Any]:
        """
        Executes all tasks while respecting dependencies and priorities.

        :return: Dictionary with task results and statuses.
        """
        if self._detect_circular_dependencies():
            raise ValueError("❌ Circular dependencies detected")

        results = {}
        completed = set()
        futures = {}

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            while len(completed) < len(self.tasks):
                ready_tasks = []

                # Select tasks ready for execution (no unmet dependencies)
                for task_id, task in self.tasks.items():
                    if (
                        task["status"] == "pending"
                        and task["dependencies"].issubset(completed)
                    ):
                        ready_tasks.append((task["priority"], task_id))

                ready_tasks.sort()  # Lower number = higher priority

                # Submit ready tasks to the executor
                for _, task_id in ready_tasks:
                    if task_id not in futures:
                        self.tasks[task_id]["status"] = "running"
                        future = executor.submit(self.tasks[task_id]["func"])
                        futures[task_id] = future

                # Check for task completion
                for task_id in list(futures.keys()):
                    future = futures[task_id]
                    if future.done():
                        try:
                            result = future.result()
                            results[task_id] = {
                                "status": "success",
                                "result": result,
                            }
                        except Exception as e:
                            results[task_id] = {
                                "status": "failed",
                                "error": str(e),
                            }

                        self.tasks[task_id]["status"] = results[task_id]["status"]
                        completed.add(task_id)
                        del futures[task_id]

        return results


# Example usage (can be removed in test-ready version)
if __name__ == "__main__":
    scheduler = TaskScheduler(max_workers=2)

    def task_a():
        time.sleep(0.1)
        return "Task A completed"

    def task_b():
        time.sleep(0.1)
        return "Task B completed"

    def task_c():
        time.sleep(0.1)
        return "Task C completed"

    def task_d():
        time.sleep(0.1)
        return "Task D completed"

    scheduler.add_task("A", priority=1, dependencies=[], execution_func=task_a)
    scheduler.add_task("B", priority=2, dependencies=["A"], execution_func=task_b)
    scheduler.add_task("C", priority=1, dependencies=["A"], execution_func=task_c)
    scheduler.add_task("D", priority=3, dependencies=["B", "C"], execution_func=task_d)

    results = scheduler.execute()

    print("✅ Execution Results:")
    for tid, res in results.items():
        print(f"  {tid}: {res}")
