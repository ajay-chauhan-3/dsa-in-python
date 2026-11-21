"""
Link: https://leetcode.com/problems/find-subtree-sizes-after-changes/

Time Complexity: O(n)
- Making the adjacency list takes O(n) time, and DFS visits every node once in O(n) time.

Space Complexity: O(n)
- Adjacency list and recursion stack take O(n) space, while lastseen uses fixed space of 26.

Concept:
- Keep track of the nearest matching character above the current node while going down the tree in DFS, and remove it while coming back up so other branches don't see it.
- Calculate subtree sizes from bottom to top: since children finish first, a node already has its final size ready before passing it up to its new parent.
"""


def findSubtreeSizes(parent, s):
    n = len(parent)
    adj = [[] for _ in range(n)]

    for i in range(1, n):
        adj[parent[i]].append(i)

    # Stores the nearest ancestor for each character 'a'-'z' on the current path
    lastseen = [-1] * 26
    size = [1] * n

    def dfs(cur_node):
        ch = ord(s[cur_node]) - 97

        # Save the previous ancestor having the same character
        closest_ancestor = lastseen[ch]

        # Update current node as the nearest ancestor for its children
        lastseen[ch] = cur_node

        for child in adj[cur_node]:
            dfs(child)

        # Put the old ancestor back when leaving this node 
        lastseen[ch] = closest_ancestor

        # Skip root (node 0) because root has no parent (parent[0] = -1)
        # Also, all children of cur_node are already done, so size[cur_node] is final now
        if cur_node != 0:
            cur_parent = parent[cur_node]

            # If a matching ancestor exists above, change parent to that ancestor
            if closest_ancestor != -1:
                cur_parent = closest_ancestor
                parent[cur_node] = cur_parent

            # Add cur_node's final subtree size to whichever parent it is attached to
            size[cur_parent] += size[cur_node]

    dfs(0)
    return size