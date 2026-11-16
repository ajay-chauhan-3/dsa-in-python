"""
Link: https://www.geeksforgeeks.org/problems/the-pattern-matcher/1

Time Complexity: O(n)
- Single pass; each character is visited once

Space Complexity: O(1)
- Constant extra variables

Concept:
- Run-length balance check: count consecutive 'x's (+1) followed by consecutive 'y's (-1), verifying each block results to 0.
"""

def findPattern(s):
    
    n = len(s)
    i = x_count = 0
    
    while i<n:
        
        while i<n and s[i]=='x':
            x_count += 1
            i+=1
            
        while i<n and s[i] == 'y':
            x_count -= 1
            i+=1
            
        if x_count:
            return False
            
    return True