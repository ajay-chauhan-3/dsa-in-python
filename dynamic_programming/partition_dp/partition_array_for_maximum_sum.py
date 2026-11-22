"""
Link: https://leetcode.com/problems/partition-array-for-maximum-sum/

Time Complexity:
- Top-Down: O(n * k) — n states, each checking up to k partition lengths.
- Bottom-Up: O(n * k) — n indices, each checking up to k partition lengths.

Space Complexity:
- Top-Down: O(n) — dp array and recursion call stack each take O(n) space.
- Bottom-Up: O(n) — dp array takes O(n) space.

Concept:
- Top-Down (Memoization):
  - Try every valid partition length from 1 to k starting at each index using recursion with memoization.
  - Why it works: A greedy choice fails because extending a subarray can include a larger element that increases the value of earlier elements.
  - Different partition paths reach the same remaining suffix, so caching results in dp avoids redundant calculations.

- Bottom-Up (Tabulation):
  - Solve from right to left using Bottom-Up DP, where dp[i] stores the maximum sum for the subarray starting at index i.
  - Why it works: Solving smaller suffixes first ensures the optimal sum for the remaining array is already available when testing partition lengths from 1 to k at index i.
"""

# Solution 1 : Top-Down (Memoization)
def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [-1]*n

    def dfs(i):
        if i>=n:
            return 0

        if dp[i]!=-1:
            return dp[i]

        cur_max = 0
        total_sum = 0
    
        for j in range(i,min(n,i+k)):
            cur_max = max(cur_max,arr[j])
            cur_sum = cur_max*(j-i+1)
            total_sum = max(total_sum, cur_sum + dfs(j+1))

        dp[i] = total_sum
        return total_sum

    return dfs(0)
    

# Solution 2 : iterative {Bottom-Up (Tabulation)}
def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0]*(n+1)

    for i in range(n-1,-1,-1):
        cur_max = 0
        for j in range(i,min(n,i+k)):
            cur_max = max(cur_max,arr[j])
            cur_sum = cur_max*(j-i+1)
            dp[i] = max(dp[i], cur_sum + dp[j+1])

    return dp[0]