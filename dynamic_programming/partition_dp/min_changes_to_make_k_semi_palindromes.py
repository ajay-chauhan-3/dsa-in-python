"""
Link: https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/

Time Complexity: O(n^3 * d(n) + n^2 * k)  [where d(n) = number of divisors of n, ~ O(n^(1/3))]
- Semi-palindrome cost computation (both Memoized & Tabulated):
  - O(n^2) substrings (i, j) of length L <= n.
  - For each divisor div of L, total elements across all div groups = L -> O(L) work per divisor.
  - Across all divisors of L -> O(L * d(L)) per substring -> O(n^3 * d(n)) total.
- Partition DP (both Top-Down & Bottom-Up):
  - States = n * k, transition loop over split point j takes O(n) -> O(n^2 * k).

Space Complexity:
- Solution 1 (Top-Down Memoization): O(n^2 + n * k)
  - pal_cost table = O(n^2), dp table = O(n * k), recursion call stack = O(k).
- Solution 2 (Bottom-Up Tabulation): O(n^2 + n * k)
  - pal_cost table = O(n^2), dp table = O(n * k), no recursion stack.

Concept:
- Break the problem into two parts: 
    - first find the minimum changes needed to make any substring s[i..j] a semi-palindrome by checking all valid divisors of its length and comparing characters at step = div using two pointers.
    - Then use Partition DP to split the string into k parts (each of length at least 2) so the total changes across all parts are minimized.
"""

# Method 1 : Top-Down Memoization


def minimumChanges(s, k):

    INF = float('inf')

    n = len(s)

    pal_cost = [[-1]*(n) for _ in range(n)]

    def semi_pal_cost(start,end):

        if pal_cost[start][end]!=-1:
            return pal_cost[start][end]

        length = end - start + 1

        min_cost = INF

        for div in range(1,length):
            if length % div != 0:
                continue
            cost = 0
            for group in range(div):

                left = start + group
                # right = (math.ceil((end+1-left)/div) - 1) * div + left
                right = ((end-left)//div)  * div + left

                while left<right:
                    if s[left]!=s[right]:
                        cost += 1

                    left += div
                    right -= div

            min_cost = min(min_cost,cost)  
        pal_cost[start][end] = min_cost

        return min_cost  
    

    dp = [[-1]*(k+1) for _ in range(n)]

    def dfs(i,k_left):

        if k_left == 0:
            if i>=n:
                return 0
            return INF

        if n < 2*k_left + i:
            return INF

        if dp[i][k_left]!=-1:
            return dp[i][k_left]

        cost = INF
        for j in range(i+1,n):

            rem_cost = dfs(j+1,k_left-1)

            if rem_cost == INF:
                continue

            cur_cost = semi_pal_cost(i,j)
            cost = min(cost,rem_cost + cur_cost)

        dp[i][k_left] = cost

        return cost

    return dfs(0,k)


# Method 2: Bottom-Up Tabulation

def minimumChanges(s, k):

    INF = float('inf')

    n = len(s)

    pal_cost = [[-1]*(n) for _ in range(n)]

    def semi_pal_cost(start,end):

        length = end - start + 1

        min_cost = INF

        for div in range(1,length):
            if length % div != 0:
                continue
            cost = 0
            for group in range(div):

                left = start + group
                # right = (math.ceil((end+1-left)/div) - 1) * div + left
                right = ((end-left)//div)  * div + left

                while left<right:
                    if s[left]!=s[right]:
                        cost += 1

                    left += div
                    right -= div

            min_cost = min(min_cost,cost) 
        return min_cost 

    # cal cost for making s[i..j] semi-pal
    for i in range(n):
        for j in range(i+1,n):
            pal_cost[i][j] = semi_pal_cost(i,j)

    
    dp = [[INF]*(k+1) for _ in range(n+1)]
    dp[n][0] = 0

    for i in range(n-1,-1,-1):
        for k_left in range(1,k+1):

            if n < 2*k_left + i:
                continue

            cost = INF
            for j in range(i+1,n):

                rem_cost = dp[j+1][k_left-1]

                if rem_cost == INF:
                    continue

                cur_cost = pal_cost[i][j]
                cost = min(cost,rem_cost + cur_cost)

            dp[i][k_left] = cost

    return dp[0][k]