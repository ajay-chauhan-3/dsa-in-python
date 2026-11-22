"""
Link: https://leetcode.com/problems/split-array-largest-sum/

Time Complexity: O(n^2 * k)
- There are n * k possible states (index i and remaining splits k_left).
- Each state runs a loop up to n times to try all valid split points, taking O(n) time per state.

Space Complexity: O(n * k)
- The dp table takes O(n * k) space.
- The recursion call stack takes O(k) space.

Concept:
- Use recursion with memoization (Top-Down DP) to try all possible ways to split the array into k parts.
- Why it works: Greedy does not work when we need exact k splits, so we check every valid split point and pick the one with the smallest max sum.
- Different split paths reach the same remaining array and remaining splits, so saving those results avoids solving the same subproblem again.
"""



def splitArray(nums, k):
    n = len(nums)
    dp = [[-1] * (k + 1) for _ in range(n)]

    def dfs(i, k_left):
        if i == n:
            if k_left == 0:
                return 0
            return float('inf')

        if k_left == 0 or k_left > n - i:
            return float('inf')

        if dp[i][k_left] != -1:
            return dp[i][k_left]

        cur_sum = 0
        min_sum = float('inf')

        for j in range(i, n - k_left + 1):
            cur_sum += nums[j]

            # Pruning: if current subarray sum already beats min_sum, larger j will only make it worse
            if cur_sum >= min_sum:
                break

            cur_max = max(cur_sum, dfs(j + 1, k_left - 1))
            min_sum = min(min_sum, cur_max)

        dp[i][k_left] = min_sum
        return min_sum

    return dfs(0, k)