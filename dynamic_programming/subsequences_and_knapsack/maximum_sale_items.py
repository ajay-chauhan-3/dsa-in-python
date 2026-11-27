"""
Link: https://leetcode.com/problems/maximum-number-of-items-from-sale-i/

Time Complexity: O(n^2 + n * budget)
- Precomputing free_items for all pairs takes O(n^2) time, and filling the 2D DP table takes O(n * budget) time.

Space Complexity: O(n * budget)
- The DP table dp[n + 1][budget + 1] uses O(n * budget) space, and free_items uses O(n) space.

Concept:
- buying the first copy of each item as a 0/1 Knapsack decision (since only the first copy gives free bonus items), then spend any remaining budget on the cheapest item.
- Why it works:
  - First copy vs. extra copies: Buying the 1st copy of item i gives (1 + free_items[i]) total copies, while every extra copy of any item gives only 1 copy with zero bonus.
  - Greedy leftover spending: Once the 0/1 choices are fixed, the best way to spend leftover money is buying as many copies of the cheapest item as possible (price_left // cheapest_price).
  - Precomputing free_items: Counting all j != i where factor[j] % factor[i] == 0 upfront lets the DP state transition in O(1) time.
"""

# solution 1: iterative / bottom-up

def maximumSaleItems(items, budget):
    
    n = len(items)
    free_items = [0]*n
    cheapest_price = float('inf')

    for i in range(n):
        copy = 0
        for j in range(n):
            cheapest_price = min(cheapest_price,items[j][1])

            if i == j:
                continue

            if items[j][0] % items[i][0] == 0:
                copy += 1

        free_items[i] = copy 

    dp = [[0]*(budget+1) for _ in range(n+1)]

    for i in range(n,-1,-1):
        for price_left in range(1,budget+1):

            if i == n:
                dp[i][price_left] = price_left//cheapest_price
                continue

            take = 0
            if price_left-items[i][1] >= 0:
                take = free_items[i] + 1 + dp[i+1][price_left-items[i][1]] 
            skip = dp[i+1][price_left]

            dp[i][price_left] =  max(take,skip)

    return dp[0][budget]


# solution 2:   Top-Down Memoization

def maximumSaleItems(items, budget):
    n = len(items)

    free_items = [0]*n

    cheapest_price = float('inf')

    for i in range(n):
        copy = 0
        for j in range(n):
            cheapest_price = min(cheapest_price,items[j][1])

            if i == j:
                continue

            if items[j][0] % items[i][0] == 0:
                copy += 1

        free_items[i] = copy 

    dp = [[-1]*(budget+1) for _ in range(n)]

    def dfs(i,budget):
        if budget <= 0:
            return 0
        if i >= n: # in the end buying cheapest items gives max items if there is budget left
            return budget//cheapest_price

        if dp[i][budget]!=-1:
            return dp[i][budget]

        take = 0
        if budget-items[i][1] >= 0:
            take = free_items[i] + 1 + dfs(i+1,budget-items[i][1])
        skip = dfs(i+1,budget)

        dp[i][budget] =  max(take,skip)
        return dp[i][budget]

    return dfs(0,budget)
                         
                