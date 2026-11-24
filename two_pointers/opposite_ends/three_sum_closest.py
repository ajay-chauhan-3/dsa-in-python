"""
Link: https://leetcode.com/problems/3sum-closest/

Time Complexity: O(n^2) + nlog(n)
- Sorting takes O(n log n).
- Outer loop runs O(n) times, and inner two-pointer scan takes O(n) per iteration -> O(n^2).

Space Complexity: O(1)
- In-place sorting and constant extra variables (O(n) worst-case auxiliary space used internally by Python's Timsort).

Concept:
- Sort the array to enable directional pointer movement based on sum comparison.
- Fix one number and run opposite-direction two pointers on the remaining subarray to minimize abs(target - sum).
"""

def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)

    best_sum = 0
    min_distance = float('inf')

    for i in range(n - 2):
        if i>0 and nums[i] == nums[i-1]:
            continue
        new_target = target - nums[i]

        left = i + 1
        right = n - 1
        while left < right:
            cur_sum = nums[left] + nums[right]
            cur_distance = abs(new_target - cur_sum)

            if cur_distance == 0:
                return cur_sum + nums[i]

            if cur_distance < min_distance:
                min_distance = cur_distance
                best_sum = cur_sum + nums[i]

            if cur_sum < new_target:
                left += 1
            else:
                right -= 1

    return best_sum