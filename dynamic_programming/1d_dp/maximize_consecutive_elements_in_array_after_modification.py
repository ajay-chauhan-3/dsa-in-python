"""
Link: https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/

Time Complexity:
- Solution 1 (Top-Down DP + Binary Search): O(n log n)
  - Sorting takes O(n log n), 2n states each doing two binary searches of O(log n).
- Solution 2 (Bottom-Up Iterative DP + Binary Search): O(n log n)
  - Sorting takes O(n log n), n * 2 loop with two binary searches per state.
- Solution 3 (Optimized Bottom-Up DP - Reusing Binary Search): O(n log n)
  - Sorting takes O(n log n), reduces binary searches from 4 to 3 per index by reusing the lookup for x + 1.
- Solution 4 (Top-Down DP - Linear Scan / Less Preferred): O(n log n)
  - Sorting takes O(n log n), 2n states each doing O(1) transitions.

Space Complexity:
- Solution 1: O(n)
  - DP table takes O(2n) and recursion call stack takes O(n).
- Solution 2: O(n)
  - DP table takes O(2n), no recursion stack.
- Solution 3: O(n)
  - DP table takes O(2n), no recursion stack.
- Solution 4: O(n)
  - DP table takes O(2n) and recursion call stack takes O(n).

Concept:
- Order of elements in the input does not matter since selected elements must form a consecutive sequence.
- Sort the array first so consecutive values appear in increasing order.
- Each element x can either stay as x (p = 0) or become x + 1 (p = 1).
- Use DP where state (i, p) tracks the longest consecutive chain starting from index i with state p, jumping to the next required value (cur + 1) using binary search.
"""


# Solution 1: Top-Down DP + Binary Search (Intuitive)
# Concept:
# - Start at index i with state p (0 means unchanged, 1 means incremented), giving current value cur = nums[i] + p.
# - To extend the consecutive chain to cur + 1, binary search ahead for either (cur + 1) (kept p unchanged i.e 0), or (cur) incremented by 1.

def maxSelectedElements(nums):
    n = len(nums)
    nums.sort()
    dp = [[-1] * 2 for _ in range(n)]

    def dfs(i, p):
        if i >= n:
            return 0

        if dp[i][p] != -1:
            return dp[i][p]

        length = 1
        cur = nums[i] + p

        j = bisect_left(nums, cur + 1, lo=i + 1)
        if j < n and nums[j] == cur + 1:
            length = 1 + dfs(j, 0)

        j = bisect_left(nums, cur, lo=i + 1)
        if j < n and nums[j] == cur:
            length = max(length, 1 + dfs(j, 1))

        dp[i][p] = length
        return length

    res = 1
    for i in range(n):
        res = max(res, dfs(i, 0), dfs(i, 1))

    return res


# Solution 2: Bottom-Up Iterative DP + Binary Search
# Concept:
# - Direct iterative conversion of Solution 1 to remove recursion overhead.
# - Fill the DP table from right to left (n - 1 down to 0) for both states p = 0 and p = 1.

def maxSelectedElements(nums):
    n = len(nums)
    nums.sort()

    def get_target(l, r, target):
        l = bisect_left(nums, target, lo=l)
        if l < n and nums[l] == target:
            return l
        return -1

    dp = [[1] * 2 for _ in range(n + 1)]
    dp[n][0] = dp[n][1] = 0
    res = 0

    for i in range(n - 1, -1, -1):
        for p in range(2):
            length = 1
            cur = nums[i] + p

            j = get_target(i + 1, n, cur + 1)
            if j != -1:
                length = 1 + dp[j][0]

            j = get_target(i + 1, n, cur)
            if j != -1:
                length = max(length, 1 + dp[j][1])

            dp[i][p] = length
            res = max(res, length)

    return res


# Solution 3: Optimized Bottom-Up DP (Reusing Binary Search)
# Concept:
# - Unroll the inner p loop in Solution 2.
# - For x = nums[i], p = 0 looks for (x + 1, 0) or (x, 1), while p = 1 looks for (x + 2, 0) or (x + 1, 1).
# - Reuse the binary search index of (x + 1) across both p = 0 and p = 1 to avoid redundant lookups.

def maxSelectedElements(nums):
    n = len(nums)
    nums.sort()

    def get_target(l, r, target):
        l = bisect_left(nums, target, lo=l)
        if l < n and nums[l] == target:
            return l
        return -1

    dp = [[1] * 2 for _ in range(n + 1)]
    dp[n][0] = dp[n][1] = 0
    res = 0

    for i in range(n - 1, -1, -1):
        x = nums[i]

        j1 = get_target(i + 1, n, x + 1)
        if j1 != -1:
            dp[i][0] = max(dp[i][0], 1 + dp[j1][0])

        j2 = get_target(i + 1, n, x)
        if j2 != -1:
            dp[i][0] = max(dp[i][0], 1 + dp[j2][1])

        j3 = get_target(i + 1, n, x + 2)
        if j3 != -1:
            dp[i][1] = max(dp[i][1], 1 + dp[j3][0])

        if j1 != -1:
            dp[i][1] = max(dp[i][1], 1 + dp[j1][1])

        res = max(res, dp[i][1], dp[i][0])

    return res


# Solution 4: Top-Down DP - Adjacent Comparison (Less Preferred)
# Concept:
# - Step index-by-index instead of jumping via binary search, comparing nums[i] against the previous picked value (prev = nums[i - 1] + p).
# - Either pick nums[i] (if nums[i] == prev + 1 or nums[i] + 1 == prev + 1) or skip duplicate elements (if nums[i] == nums[i - 1], carry state p forward).
# - Less intuitive because skipping duplicates requires careful state forwarding and starting the chain cleanly from every index.

def maxSelectedElements(nums):
    n = len(nums)
    nums.sort()
    dp = [[-1] * 2 for _ in range(n)]

    def dfs(i, p):
        if i >= n:
            return 0

        if dp[i][p] != -1:
            return dp[i][p]

        res = 0
        prev = nums[i - 1] + p

        if nums[i] == prev + 1:
            res = 1 + dfs(i + 1, 0)
        elif nums[i] + 1 == prev + 1:
            res = 1 + dfs(i + 1, 1)

        if nums[i] == nums[i - 1]:
            res = max(res, dfs(i + 1, p))

        dp[i][p] = res
        return res

    res = 1
    for i in range(n):
        res = max(res, 1 + dfs(i + 1, 0), 1 + dfs(i + 1, 1))

    return res