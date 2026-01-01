"""
Rate Limiter - Sliding Window Log Algorithm
-------------------------------------------
This implementation allows up to `max_requests` in a given time window (in seconds)
for each user. It tracks timestamps per user and uses a sliding window log mechanism.

Concurrency-safe with locking.
"""

from collections import defaultdict
from time import time
from threading import Lock


class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        """
        Initialize the rate limiter.

        :param max_requests: Maximum allowed requests per user
        :param window_seconds: Time window in seconds
        """
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = defaultdict(list)  # user_id -> list of request timestamps
        self.lock = Lock()  # Ensures thread-safe access

    def allow_request(self, user_id: str) -> bool:
        """
        Check if the request from user_id is allowed based on sliding window log.

        :param user_id: The identifier for the requesting user
        :return: True if allowed, False if rate limit exceeded
        """
        with self.lock:
            current_time = time()
            window_start = current_time - self.window_seconds

            # Remove old requests outside the time window
            recent_requests = [
                timestamp for timestamp in self.requests[user_id]
                if timestamp > window_start
            ]
            self.requests[user_id] = recent_requests

            # Allow request if under limit
            if len(recent_requests) < self.max_requests:
                self.requests[user_id].append(current_time)
                return True

            return False

    def cleanup_user(self, user_id: str) -> None:
        """
        Manually cleanup a user's request history to free memory.

        :param user_id: The identifier of the user to clean up
        """
        with self.lock:
            if user_id in self.requests:
                del self.requests[user_id]


## from rate_limiter import RateLimiter

limiter = RateLimiter(3, 10)
for i in range(5):
    print("Request allowed:", limiter.allow_request("user42"))
