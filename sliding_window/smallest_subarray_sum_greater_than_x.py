"""
Link: https://www.geeksforgeeks.org/problems/smallest-subarray-with-sum-greater-than-x5651/1

Time Complexity: O(n)
- Each element is added and removed at most once by the two pointers.

Space Complexity: O(1)
- Constant extra variables.

Concept:
- Variable-size sliding window (works since elements are positive):
  - Expand right pointer to grow the subarray sum.
  - Once the sum exceeds x, shrink from the left while keeping the sum strictly greater than x, tracking the minimum window length at each step.
"""

def smallestSubWithSum(arr, x):
    n = len(arr)
    total = i = j = 0
    res = n + 1

    while j < n:
        total += arr[j]

        while total > x:
            res = min(res, j - i + 1)
            total -= arr[i]
            i += 1

        j += 1

    return res if res != n + 1 else 0