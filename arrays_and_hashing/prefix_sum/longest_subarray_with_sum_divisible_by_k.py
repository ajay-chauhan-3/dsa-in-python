"""
Link: https://www.geeksforgeeks.org/problems/longest-subarray-with-sum-divisible-by-k1259/1

Time Complexity: O(n)
- Single pass through the array with O(1) average hash map lookups and insertions.

Space Complexity: O(min(n, k))
- Hash map stores at most k different remainders (and at most n entries).

Concept:
- Keep adding numbers from the start and take the remainder with k at each index.
- If the current remainder matches a remainder seen at an earlier index, the subarray between those two indexes is divisible by k.
- This happens because subtracting two sums with the same remainder cancels out the extra remainder, leaving a multiple of k.
- Save only the first index of each remainder so we get the longest subarray..
"""

def longestSubarrayDivK(arr, k):
    n = len(arr)

    prev_ps = {0: -1}
    ps = 0
    res = 0

    for i in range(n):
        ps += arr[i]
        ps = ps % k

        if ps in prev_ps:
            res = max(res, i - prev_ps[ps])
        else:
            prev_ps[ps] = i

    return res