"""
Link: https://www.geeksforgeeks.org/problems/min-number-of-flips3210/1

Time Complexity: O(n)
- Single pass over the string of length n.

Space Complexity: O(1)
- Constant extra variables used.

Concept:
- A binary alternating string has only two possible patterns: starting with '0' ("0101...") or starting with '1' ("1010...").
- Count flips needed to match the "0101..." pattern (zero_flip).
- Since both patterns are exact opposites at every index, flips needed for "1010..." is simply `n - zero_flip`. Return the minimum of the two.
"""

def minFlips(s):
    # Code here
    n = len(s)
    zero_flip = 0
    
    for i in range(n):
        ch = '1' if i&1 else '0'
        
        if s[i]!=ch:
            zero_flip += 1
            
    return min(zero_flip,n-zero_flip)
