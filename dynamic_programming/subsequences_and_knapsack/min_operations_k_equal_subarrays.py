"""
Link: https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/

Time Complexity: O(n log x + n * k)
- Sliding window median cost: n iterations, each SortedList add/remove/pop takes O(log x) -> O(n log x).
- DP (both Bottom-Up & Top-Down): (n - x + 1) * k states, O(1) transition per state -> O(n * k).

Space Complexity: O(n * k)
- Sliding window SortedLists hold at most x elements -> O(x).
- Cost array takes O(n), and DP table takes O(n * k) (plus O(n) recursion stack in Top-Down).

Concept:
- To make all elements in a window of size x equal with minimum operations, change every element to the window's median.
- Use a sliding window with two SortedLists (left and right halves) to dynamically maintain the median and compute the cost for every subarray of size x in O(log x).
- Once window costs are ready, use take/skip DP (pick current window and jump by x, or skip to i + 1) to select k non-overlapping subarrays with minimum total cost.
"""


from sortedcontainers import SortedList
import sys
sys.setrecursionlimit(200000)


def minOperations(nums, x, k):

    n = len(nums)

    left = SortedList()
    right = SortedList()

    left_sum = right_sum = 0
    cost = [0] * (n - x + 1)

    for i in range(n):
        v = nums[i]
        if right and v>right[0]:
            right.add(v)
            right_sum += v
        else:
            left.add(v)
            left_sum+=v

        while len(left) > len(right)+1:
            last = left.pop(-1)
            left_sum -= last

            right.add(last)
            right_sum += last

        while len(left)<len(right):
            val = right.pop(0)
            right_sum -= val

            left.add(val)
            left_sum+=val

        if len(left)+len(right) == x:
            mid = left[-1]
            cost[i-x+1] = len(left)*mid - left_sum + right_sum - len(right)*mid

            first = nums[i-x+1]

            if first<=mid:
                left.remove(first)
                left_sum -= first
            else:
                right.remove(first)
                right_sum -= first

    m = n-x+1
    dp = [[float('inf')]*(k+1) for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = 0

    for i in range(m-1,-1,-1):
        for k_left in range(1,k+1):

            dp[i][k_left] = min(dp[i+1][k_left],cost[i] + dp[i+x][k_left-1])

    return dp[0][k]


    # dp = [[-1]*(k+1) for _ in range(n-x+1)]

    # def dfs(i,k_left):
    #     if k_left == 0:
    #         return 0

    #     if i>= n - x + 1:
    #         return float('inf')

    #     if dp[i][k_left]!=-1:
    #         return dp[i][k_left]

    #     z = dfs(i+1,k_left)
    #     y = cost[i] + dfs(i+x,k_left-1)

    #     dp[i][k_left] = min(z,y)

    #     return dp[i][k_left]

    # return dfs(0,k)
    