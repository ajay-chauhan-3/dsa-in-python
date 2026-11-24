"""
Link: https://www.geeksforgeeks.org/problems/satisfy-the-equation5847/1

Time Complexity: O(n^2)
- Two nested loops check all pairs (i, j) with i < j, and hash map lookup takes O(1) time.

Space Complexity: O(n^2)
- In the worst case, every pair sum is unique, storing up to O(n^2) pairs in the map.

Concept:
- Generate all pairs (i, j) in order and save the first pair for each sum in a hash map.
- Why it works:
  - First seen pair is smallest: Loops run from left to right (i from 0, j from i + 1), so pairs come in exact lexicographical order. Keeping only the first pair for a sum ensures (a, b) is always the smallest possible.
  - Distinct indices check: When the same sum repeats at (i, j), checking a != i, a != j, b != i, and b != j avoids reusing the same element.
  - Tracking global best: A sum found later might still give a smaller quadruplet [a, b, i, j] than an earlier sum, so we always keep the minimum candidate.
"""


def findPairs(arr):
    
    n = len(arr)
    pairs = {}
    best = None
    
    for i in range(n):
        for j in range(i+1,n):
            cur_sum = arr[i]+arr[j]
            
            if cur_sum in pairs:
                a,b = pairs[cur_sum]
                
                if a!=i and a!=j and b!=i and b!=j:
                    
                    candidate = [a,b,i,j]
                    if best is None or candidate<best:
                        best = candidate
            else:
                pairs[cur_sum] = (i,j)
                
    return best if best else [-1,-1,-1,-1]
                        
                    
                    
                    
        