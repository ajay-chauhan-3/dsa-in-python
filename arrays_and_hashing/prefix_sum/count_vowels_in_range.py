"""
Link: https://www.geeksforgeeks.org/problems/range-vowel-count-queries-static/1

Time Complexity: O(n + q)
- Building the prefix sum array takes O(n) time, and each of the q queries takes O(1) time.

Space Complexity: O(n)
- Prefix sum array ps uses O(n) extra space.

Concept:
- Store running vowel counts in a prefix sum array ps (size n + 1), then answer each query [l, r] in O(1) using ps[r + 1] - ps[l].
- Why it works:
  - Range subtraction: ps[r + 1] holds vowels from 0 to r, and ps[l] holds vowels from 0 to l - 1. Subtracting them leaves exact vowels in [l, r].
  - Dummy 0 at start: Using ps[0] = 0 avoids any if/else check when l = 0.
"""

def countVowels(s, queries):
    
    n = len(s)
    
    ps = [0]*(n+1)
    
    for i in range(1,n+1):
        ps[i] = ps[i-1]
        if s[i-1] in 'aeiou':
            ps[i] += 1
        
    res = []      
    for l,r in queries:
        res.append(ps[r+1]-ps[l])
        
    return res
            
