"""
Link: https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

Time Complexity: O(n)   # single pass through the array with O(1) work per element
Space Complexity: O(1)  # Only tracks running prefix sum and parity counters

Concept:
- Mathematical Formulation (Prefix Sum Parity):
  - Subarray sum(l..i) = ps[i] - ps[l - 1].
  - difference is ODD only when both prefix sums have OPPOSITE parity:
    (Odd - Even = Odd) or (Even - Odd = Odd)
  - Thus, a subarray ending at 'i' is odd if we pair `ps[i]` with any previous prefix sum of opposite parity.
  - Base Case: `even_count = 1` initially to represent `ps[-1] = 0` (handles subarrays starting at index 0).

- Method 2 (Combinatorics Shortcut: `odd_count * even_count`):
  - Every valid odd subarray is formed by picking 1 Odd prefix sum and 1 Even prefix sum.
  - Why index order doesn't matter in multiplication:
    Pick any one odd index and any one even index—whichever index appears earlier in the array naturally acts as `l - 1` (start) and the later one acts as `i` (end), always forming a valid subarray.
"""


# Method 1: Running prefix sum pairing
def numOfSubarrays(arr):
    even_count = 1
    odd_count = ps = 0
    mod = 10**9 + 7
    res = 0

    for x in arr:
        ps += x
        if ps & 1:  # odd prefix sum pairs with all previous even prefix sums
            res += even_count
            odd_count += 1
        else:       # even prefix sum pairs with all previous odd prefix sums
            res += odd_count
            even_count += 1
        res %= mod

    return res


# Method 2: Total odd * even combinations
def numOfSubarraysMath(arr):
    even_count = 1
    odd_count = ps = 0
    mod = 10**9 + 7

    for x in arr:
        ps += x
        if ps & 1:
            odd_count += 1
        else:
            even_count += 1

    return (even_count * odd_count) % mod


