"""
Link: https://www.geeksforgeeks.org/problems/minimal-cost/1

Time Complexity: O(n * k)
- There are n states (indexes 0 to n - 1), and each state loops over at most k next stones.

Space Complexity: O(n)
- The dp array and recursion call stack each take O(n) space.

Concept:
- To find the minimum cost from stone i to the end, we need to try all valid jumps from i + 1 up to i + k and pick the cheapest path.
- Greedy does not work here because a cheap jump now can land on a stone that forces a very costly jump later.
- Many different jump paths reach the same stone i, so we save the minimum cost from stone i in a dp array to avoid solving the same index again.
"""


def minimizeCost(k, arr):
    n = len(arr)
    dp = [-1]*n
    
    def dfs(i):
        
        if i == n-1:
            return 0
            
        if dp[i]!=-1:
            return dp[i]
        
        min_cost = float('inf')
        for j in range(i+1,min(n,i+k+1)):
            cost = abs(arr[i]-arr[j]) + dfs(j)
            min_cost = min(min_cost,cost)
            
        dp[i] = min_cost
            
        return min_cost
        
    return dfs(0)