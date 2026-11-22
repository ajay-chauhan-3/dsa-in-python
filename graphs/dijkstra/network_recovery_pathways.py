"""
Link: https://leetcode.com/problems/network-recovery-pathways/

Time Complexity: O((V + E) + (V + E * log E) * log(max_cost))
- Building the adjacency list takes O(V + E) time once.
- Binary search runs over the edge cost range in O(log(max_cost)) steps.
- In each step, initializing dist takes O(V) and Dijkstra's algorithm pushes/pops at most E edges in O(E log E) time (which simplifies to O(E log V) since E <= V^2).

Space Complexity: O(V + E)
- Adjacency list takes O(V + E) space, and the dist array + heap take O(V + E) space in the worst case.

Concept:
- Maximize the minimum edge cost along a valid path using Binary Search on Answer.
- For a candidate score mid, ignore offline nodes and edges with cost < mid, then run Dijkstra algorithm to check if node n - 1 is reachable within total cost k.
- Why it works: If destination is reachable with total cost <= k using only edges >= mid, then mid is achievable and we try a higher score; otherwise, we try lower.
"""

from heapq import heappop, heappush

def findMaxPathScore(edges, online, k):
    n = len(online)
    adj = [[] for _ in range(n)]

    l = float('inf')
    r = 0

    for u, v, c in edges:
        if online[u] and online[v]:
            adj[u].append((v, c))
            l = min(l, c)
            r = max(r, c)

    if l == float('inf'):
        return 0 if n == 1 else -1

    def check(mid):
        dist = [float('inf')] * n
        heap = [(0, 0)]
        dist[0] = 0

        while heap:
            d, node = heappop(heap)

            if d > k:
                return False

            if node == n - 1:
                return True

            if d > dist[node]:
                continue

            for child, w in adj[node]:
                if w < mid:
                    continue

                nd = w + d
                if nd < dist[child]:
                    heappush(heap, (nd, child))
                    dist[child] = nd

        return False

    ans = -1
    while l <= r:
        mid = (l + r) // 2

        if check(mid):
            ans = mid
            l = mid + 1
        else:
            r = mid - 1

    return ans