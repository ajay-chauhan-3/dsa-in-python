"""
Link: https://www.geeksforgeeks.org/problems/print-common-nodes-in-bst/1

Note:
- This is just an implementation of the core function.
- To run this locally, construct two BSTs and pass their root nodes to the function.

Time Complexity: O(n1 + n2)   # each node in r1 and r2 is pushed and popped at most once
Space Complexity: O(h1 + h2)  # stacks hold at most h1 and h2 (tree heights) nodes at any time

Concept:
- Perform simultaneous iterative inorder traversal on both BSTs using two stacks (sorted order)
- Compare stack tops like a two-pointer merge on sorted arrays:
  - Equal: record value, pop both stacks, and move both pointers to their right subtrees
  - Unequal: pop the stack with the smaller value and move that pointer to its right subtree
"""

''' 
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

def findCommon(r1, r2):
    
    res = []
    stack1 = []
    stack2 = []
    
    s1 = r1
    s2 = r2
    
    while (s1 or len(stack1)>0 ) and (s2 or len(stack2)>0):
        
        while s1:
            stack1.append(s1)
            s1 = s1.left
            
        while s2:
            stack2.append(s2)
            s2 = s2.left
            
        top1 = stack1[-1]
        top2 = stack2[-1]
        
        if top1.data == top2.data:
            res.append(top1.data)
            
            stack1.pop()
            stack2.pop()
            s1 = top1.right
            s2 = top2.right
        
        elif top1.data<top2.data:
            stack1.pop()
            s1 = top1.right
        else:
            stack2.pop()
            s2 = top2.right
            
    return res
                
        