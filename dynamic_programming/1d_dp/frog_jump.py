"""
Link: https://www.geeksforgeeks.org/problems/geek-jump/1

Time Complexity: O(n)
- 3n DP states (index i and jump step p in {0, 1, 2}), each computed once in O(1) time.

Space Complexity: O(n)
- Memoization table of size n * 3 and recursion stack of depth O(n).

Concept:
- Use top-down DP tracking current stair i and the jump size p (1 or 2) used to arrive at stair i.
- Compute the arrival cost abs(arr[i] - arr[i - p]), then take the minimum total cost between jumping to i + 1 and i + 2 until reaching the last stair (n - 1).
"""

def minCost(arr):
    n = len(arr)
    
    dp = [[-1]*3 for _ in range(n)]
    
    def dfs(i,p):
        
        if i>=n:
            return float('inf')
        
        cost = 0
        if p == 1:
            cost = abs(arr[i]-arr[i-1])
        elif p == 2:
            cost = abs(arr[i]-arr[i-2])
            
        if i == n-1:
            return cost
            
        if dp[i][p]!=-1:
            return dp[i][p]
                
        ans = min(cost + dfs(i+1,1),cost + dfs(i+2,2))
        dp[i][p] = ans
        return ans
        
    return dfs(0,0)
                