"""
Link: https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/

Time Complexity: O(n)   # each group is pushed and popped from the deque at most once, and pointer 'j' only moves left
Space Complexity: O(n)  # deque holds at most 'n' groups in the worst case

Concept:
- To make an array non-decreasing with minimum operations, every element must be raised at least to the maximum element seen on its left.
- If we expand our window from left-to-right, adding a new element at the right is easy, but shrinking the window from the left changes the "maximum on the left" for all remaining elements, making it hard to recalculate cost in O(1).
- Why Right-to-Left (i from n-1 to 0)?
  - When we put a new element 'nums[i]' at the front (left), it acts as the new "boss" for all smaller elements immediately to its right.
  - Instead of updating those smaller elements one by one in O(n), we group elements that share the same boss as [boss_val, count].
  - If 'nums[i]' is bigger than the next group's 'old_boss', it takes over that whole group in O(1) with extra cost: (nums[i] - old_boss) * count.
- Why Deque instead of Stack?
  - We merge smaller groups at the front (left) when 'i' moves left, and we remove single elements from the back (right) when 'cost > k' and 'j' moves left. Since we need O(1) access on both ends, we use a Deque.
"""

# Solution 1 - Moving from right to left

from collections import deque

def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
    
    n = len(nums)

    groups = deque()

    i = j = n-1
    res,cost = 0,0

    while i>=0:

        cur = [nums[i],1] # [cur_boss,its_count]
        while groups and nums[i]>=groups[0][0]:
            old_boss,count = groups.popleft()
            cost += abs(nums[i]-old_boss)*count
            cur[1]+=count

        groups.appendleft(cur)

        while cost>k:
            right_boss = groups[-1][0]
            cost -= abs(right_boss-nums[j])

            groups[-1][1]-=1

            if groups[-1][1] == 0:
                groups.pop()

            j-=1

        res += j-i+1
        i-=1

    return res


        