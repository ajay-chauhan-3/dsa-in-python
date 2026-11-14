"""
Link: https://leetcode.com/problems/minimum-positive-sum-subarray/

Dependency Note:
- Uses `sortedcontainers` (pip install sortedcontainers) to simulate a balanced BST / multiset in Python for O(log k) insertions, deletions, and binary search.

Time Complexity: O(n log(r - l + 1))  # loop runs (n - l + 1) times; SortedList holds at most (r - l + 1) elements, so add, remove, and bisect_left each take O(log(r - l + 1)) time
Space Complexity: O(n)                # O(n) for the prefix sum array 'ps', plus O(r - l + 1) for the SortedList window

Concept:
- Mathematical Formulation:
  - A subarray ending at index 'i' with length between 'l' and 'r' has a starting prefix index 'x' in the range: [i - r, i - l].
  - Subarray sum = ps[i] - ps[x].
  - We want: ps[i] - ps[x] > 0  ===>  ps[x] < ps[i].
  - To minimize (ps[i] - ps[x]) while keeping it > 0, we need to maximize 'ps[x]' such that 'ps[x]' is strictly less than 'ps[i]'.
- Why Sliding Window + SortedList?
  - As 'i' moves forward by 1, the valid range of 'x' [i - r, i - l] also shifts right by 1:
    - 'ps[i - l]' enters the valid window.
    - 'ps[i - r - 1]' leaves the valid window (when i > r).
  - Instead of checking all 'x' in [i - r, i - l] in O(r - l) time, we keep valid 'ps[x]' values in a SortedList ('box') and use binary search (`bisect_left(ps[i]) - 1`) to find the largest 'ps[x] < ps[i]' in O(log(r - l + 1)) time.
"""


from sortedcontainers import SortedList

def minimumSumSubarray(nums, l, r):
    n = len(nums)
    res = float('inf')

    ps = [0] * (n + 1)
    for i in range(1, n + 1):   # calculate prefix sum
        ps[i] = ps[i - 1] + nums[i - 1]

    box = SortedList()  # stores valid ps[x] values where x lies in [i - r, i - l]

    for i in range(l, n + 1):
        box.add(ps[i - l])

        if i > r:
            box.remove(ps[i - r - 1])

        j = box.bisect_left(ps[i]) - 1

        if j >= 0:
            res = min(res, ps[i] - box[j])

    return -1 if res == float('inf') else res