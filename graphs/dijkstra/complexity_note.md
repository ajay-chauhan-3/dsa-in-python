# Dijkstra's Algorithm — Time & Space Complexity Notes

## Basic Terms (Simple Meaning)

- **Edge Relaxation:** Checking if going through the current node gives a shorter distance to a neighbor. If yes, we update the neighbor's distance (`if dist[u] + w < dist[v]: dist[v] = dist[u] + w`).
- **Decrease-Key:** Changing the distance of a node that is already inside the heap (for example, updating `(50, node)` directly to `(30, node)`).
  - **Without Decrease-Key (Python `heapq`):** Python's `heapq` cannot search and update an old entry inside the heap. So we just push a new `(30, node)` entry and ignore the old `(50, node)` entry when it comes out later (`if d > dist[node]: continue`). Because of these extra entries, the heap can grow up to size $E$.
  - **With Decrease-Key (Indexed Priority Queue):** Updates the old entry directly in place, so each node stays in the heap at most once (max heap size = $V$).

---

## 1. Exact Complexity in Python (`heapq`)

1. **Setup (`dist` array & `adj` list):**
   - Making `dist = [inf] * V` takes $O(V)$ time.
   - Making the adjacency list from $E$ edges takes $O(V + E)$ time.
2. **Heap Push & Pop:**
   - Every time an edge gives a shorter distance, we push a new `(distance, node)` pair into the heap.
   - In the worst case, all $E$ edges are pushed and popped once. Each heap push/pop takes $O(\log E)$ time, so total heap time is $O(E \log E)$.
3. **Total Time:**
   $$\text{Time} = O(V + E + E \log E)$$
   Since $E \log E$ is always bigger than $E$, we drop $+ E$:
   $$O(V + E \log E)$$

---

## 2. Why Different Formulas Exist

### A. Why $O(E \log E)$ and $O(E \log V)$ are the same
- A normal graph (without duplicate edges) can have at most $E \le V^2$ edges.
- Taking $\log$ on both sides:
  $$\log E \le \log(V^2) = 2 \log V = O(\log V)$$
- Dropping the constant $2$, **$O(E \log E)$ becomes $O(E \log V)$**.

### B. Connected vs. Unconnected Graphs
- **Unconnected / Any Graph:** **$O(V + E \log V)$**
  - If a graph has $10^5$ nodes and $0$ edges ($E = 0$), $E \log V$ becomes $0$, but creating the `dist` array still takes $O(V)$ time. So we must keep $+ V$.
- **Connected Graph:** **$O(E \log V)$**
  - A connected graph always has at least $E \ge V - 1$ edges.
  - Here, $E \log V$ is always bigger than $V$, so we drop $+ V$.

### C. Where $O((V + E) \log V)$ comes from
1. **Easy grouping:** Since $V \le V \log V$, we can rewrite $V + E \log V$ as $V \log V + E \log V = O((V + E) \log V)$ just to put everything inside one bracket.
2. **When using Decrease-Key:** The heap has at most $V$ nodes:
   - Popping $V$ nodes takes $O(V \log V)$.
   - Updating distances for $E$ edges takes $O(E \log V)$.
   - Adding both gives $O((V + E) \log V)$.

---

## 3. Space Complexity
- **Adjacency List:** $O(V + E)$
- **`dist` Array:** $O(V)$
- **Heap:** $O(E)$ in Python `heapq` (because of duplicate entries), or $O(V)$ if using decrease-key.
- **Total Space:** **$O(V + E)$**

---

## 4. Interview Cheat Sheet

| Case | Time Complexity | Space Complexity | When to Say This |
| :--- | :--- | :--- | :--- |
| **Connected Graph (Standard)** | $O(E \log V)$ | $O(V + E)$ | Default answer in almost all interviews |
| **Unconnected / Any Graph** | $O(V + E \log V)$ or $O((V + E) \log V)$ | $O(V + E)$ | When $E$ can be $0$ or nodes are disconnected |
| **Python `heapq` (Exact)** | $O(V + E \log E)$ | $O(V + E)$ | If asked about duplicate entries in Python's heap |
| **Adjacency Matrix (No Heap)** | $O(V^2)$ | $O(V^2)$ | When almost every node is connected to every other node ($E \approx V^2$) |