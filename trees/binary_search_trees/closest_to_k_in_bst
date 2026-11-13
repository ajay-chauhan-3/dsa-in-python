"""
Link: https://www.geeksforgeeks.org/problems/find-the-closest-element-in-bst/1

Note:
- This is just an implementation of the core function.
- To run this locally, construct a BST and pass its root node to the function.

Time Complexity: O(h)   # O(log n) for balanced BST, O(n) in worst case (skewed BST). Visiting only 1 node per level
Space Complexity: O(h)  # O(log n) for balanced BST, O(n) for skewed BST due to recursion call stack

Concept:
- we can get minimum difference when the BST value will be closest to 'k'
- so we should follow the path where getting the value 'k' in BST is possible
- if 'k' < node.data -> move to left in BST
- if 'k' > node.data -> move to right in BST

"""

'''
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = self.left = None
        
'''
def minDiff(root, k):

    def dfs(root):
        
        if not root:
            return float('inf')
               
        if root.data == k:
            return 0
            
        if k>root.data:
            diff = dfs(root.right)
            
        elif k<root.data:
            diff = dfs(root.left)
            
        return min(diff,abs(root.data-k))
        
    return dfs(root)