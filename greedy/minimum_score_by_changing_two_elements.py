"""
Link: https://leetcode.com/problems/minimum-score-by-changing-two-elements/

Time Complexity: O(n log n)
- Sorting the array takes O(n log n), checking the 3 boundary cases takes O(1).

Space Complexity: O(n)
- Python's Timsort uses up to O(n) auxiliary space in the worst case (in-place sort).

Concept:
- Changing two numbers to match an existing element creates duplicates, making the low score (minimum difference) 0.
- To minimize the high score (max - min), middle elements cannot be changed since they do not shrink the range.
- With 2 changes, removing elements from the extreme ends of the sorted array leaves only 3 cases:
  1. Change 2 smallest (nums[0], nums[1] -> nums[2]) -> range = nums[-1] - nums[2]
  2. Change 2 largest (nums[-1], nums[-2] -> nums[-3]) -> range = nums[-3] - nums[0]
  3. Change 1 smallest and 1 largest (nums[0], nums[-1] -> nums[1]) -> range = nums[-2] - nums[1]
"""

def minimizeSum(nums):
    nums.sort()
    return min(nums[-2] - nums[1], nums[-3] - nums[0], nums[-1] - nums[2])
    