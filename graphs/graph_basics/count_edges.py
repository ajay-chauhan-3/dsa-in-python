"""
Link: https://www.geeksforgeeks.org/problems/count-number-of-edges-in-an-undirected-graph/1

Time Complexity:
- Approach 1 (Degree Sum): O(V) — sums the lengths of all V adjacency lists in O(1) each.
- Approach 2 (Visited Array): O(V + E) — checks all V vertices and scans all 2E neighbor entries once (since every edge is listed in 2 vertices' lists).

Space Complexity:
- Approach 1 (Degree Sum): O(1) — uses no extra memory.
- Approach 2 (Visited Array): O(V) — uses a visited array vis of size V.

Concept:
- Count undirected edges using degree sum (no self-loops) or a visited array (handles self-loops).
- Why it works:
  - Why 2E & // 2: Every edge (u, v) connects 2 vertices, so it is stored twice in adj (in adj[u] and adj[v]). Total entries = 2E, so // 2 gives E.
  - Visited array: Counts edge (u, v) at u, marks u visited, and skips it at v. Self-loops count once since u is marked after its inner loop.
"""


# Approach 1: Optimal Degree Sum (assumes no self-loops)
def countEdges(adj):
    return sum(len(edges) for edges in adj) // 2

# Approach 2: Visited Array (handles self-loops too)
def countEdges(adj):
    vis = [0] * len(adj)
    count = 0

    for u, edges in enumerate(adj):
        if not vis[u]:
            for x in edges:
                if vis[x]:
                    continue
                count += 1
            vis[u] = 1

    return count