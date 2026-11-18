"""
Link: https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/

Time Complexity:
- Solution 1 (Top-Down DP + Prefix Sum - TLE): O(n^2)
  - n/2 even states, each trying up to n/2 even split points j with O(1) prefix sum cost lookup.
- Solution 2 (Greedy Pairwise Check - Optimal): O(n)
  - Single pass checking adjacent pairs of length 2.

Space Complexity:
- Solution 1: O(n)
  - Prefix sum array, memo table, and recursion stack each take O(n).
- Solution 2: O(1)
  - Constant extra variables.

Concept:
- Any valid even-length substring (size 4, 6, 8...) can be broken into smaller valid substrings of size 2 without needing extra changes.
- Merging pairs into a bigger block never reduces the cost—for example, "1001" takes 2 changes either way, while "0011" takes 0 changes as separate pairs vs 2 changes if merged into one block.
- So we never need larger splits: just split the string into adjacent pairs (s[i-1], s[i]) and count how many pairs have mismatched characters.
"""

#  Method 1 : Top-Down DP + Prefix Sum - TLE

def minChanges(s):
    n = len(s)

    ps = [0]*(n+1)

    for i in range(1,n+1):
        ps[i] = ps[i-1]+int(s[i-1])

    dp = [-1]*(n)

    def dfs(i):
        if i == n:
            return 0

        if dp[i]!=-1:
            return dp[i]

        cost = float('inf')

        for j in range(i+2,n+1,2):
            one_count = ps[j]-ps[i]
            two_count = j-i - one_count
            min_changes = min(one_count,two_count)
            cost = min(min_changes + dfs(j), cost)
        dp[i] =  cost
        return dp[i]

    return dfs(0)

#  Method 2 : Greedy Pairwise Check

def minChanges(s): 
    n = len(s)
    cost = 0
    for i in range(1,n,2):
        if s[i]!=s[i-1]:
            cost+=1
    return cost

        