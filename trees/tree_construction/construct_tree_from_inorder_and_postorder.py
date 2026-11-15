"""
Link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

Note:
- This is just an implementation of the core function.
- To run this locally, define the `TreeNode` class and pass `inorder` and `postorder` lists to the function.

Time Complexity: O(n)   # O(n) to build HashMap + O(1) work per node (pop, map lookup, pointer math) across 'n' nodes
Space Complexity: O(n)  # O(n) to store the HashMap + O(h) recursion stack (where h is tree height, up to O(n) in skewed tree)

Concept:
- Postorder is [Left, Right, Root], so `postorder.pop()` always gives the current root.
- Find this root's index in `inorder` ([Left, Root, Right]) in O(1) using a HashMap to split left and right subtrees.
- Build the RIGHT subtree before the LEFT subtree because popping from the end of `postorder` gives Right subtree nodes before Left.
- Pass index pointers `(l, r)` instead of slicing the array to keep work per node O(1).
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def buildTree(inorder, postorder):
    
    inorder_pos = { x:i for i,x in enumerate(inorder)}

    def divide(l,r):

        if l>r:
            return None

        root_val = postorder.pop()

        mid = inorder_pos[root_val] 

        right = divide(mid+1,r)
        left = divide(l,mid-1)

        return TreeNode(root_val,left,right)

    return divide(0,len(inorder)-1)