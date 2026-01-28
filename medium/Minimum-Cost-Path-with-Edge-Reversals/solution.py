import heapq

class Solution(object):
    def minCost(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        # Build adjacency list
        adj = [[] for _ in range(n)]

        for u, v, w in edges:
            # Normal direction
            adj[u].append((v, w))
            # Reversed direction (using switch at v)
            adj[v].append((u, 2 * w))

        INF = float('inf')
        dist = [INF] * n
        dist[0] = 0

        pq = [(0, 0)]  # (cost, node)

        while pq:
            cost, node = heapq.heappop(pq)

            if cost > dist[node]:
                continue

            for nxt, w in adj[node]:
                new_cost = cost + w
                if new_cost < dist[nxt]:
                    dist[nxt] = new_cost
                    heapq.heappush(pq, (new_cost, nxt))

        return dist[n - 1] if dist[n - 1] != INF else -1
