"""
Link: https://leetcode.com/problems/maximum-total-subarray-value-ii/

Time Complexity: O(n + k * (log n + log k))
- Building the Segment Tree takes O(n) time.
- The loop runs k times: each step pops 1 subarray and pushes at most 2 subarrays into the heap (O(log k) time) and runs at most 2 range queries on the Segment Tree (O(log n) time).

Space Complexity: O(n + k)
- Segment Tree takes O(4n) = O(n) space.
- Visited set and max-heap store at most 2k subarrays, taking O(k) space.

Concept:
- shrinking a subarray by removing an element from the left or right, its maximum can only stay the same or go down, and its minimum can only stay the same or go up.
- So (max - min) can never increase, meaning the full array [0, n - 1] always has the biggest value.
- Any smaller subarray [l', r'] lies inside some larger subarray [l, r], so its value can never be bigger than [l, r].
- That means the next best subarray must come right after shrinking a larger one by just 1 step from the left ([l + 1, r]) or 1 step from the right ([l, r - 1]).
- Use a max-heap starting with [0, n - 1] to greedily pick the top k subarrays one by one.
- Push its two 1-step smaller subarrays each time, using a visited set to avoid duplicates and a Segment Tree to get range max and min fast.
"""


from heapq import heappush, heappop

def maxTotalValue(nums, k):
    
    n = len(nums)

    def buildST(i,l,r):

        if l == r:
            segtree[i] = (nums[l],nums[l]) #max,min
            return

        mid = (l+r)//2
        buildST(2*i+1,l,mid)
        buildST(2*i+2,mid+1,r)

        max1,min1 = segtree[2*i+1]
        max2,min2 = segtree[2*i+2]

        segtree[i] = (max(max1,max2),min(min1,min2))

    def queryST(start,end,i,l,r):
        if l>=start and r<=end:
            return segtree[i]

        mid = (l+r)//2

        if mid>=end:
            return queryST(start,end,2*i+1,l,mid)

        if start>mid:
            return queryST(start,end,2*i+2,mid+1,r)

        max1,min1 = queryST(start,end,2*i+1,l,mid)
        max2,min2 = queryST(start,end,2*i+2,mid+1,r)
        return (max(max1,max2),min(min1,min2))

    def get_diff(start,end):
        max1,min1 = queryST(start,end,0,0,n-1)
        return max1-min1

    segtree = [(0,0)]*(4*n)
    buildST(0,0,n-1)

    vis = {(0,n-1)}
    heap = [(-get_diff(0,n-1),0,n-1)]

    res = 0
    for i in range(k):
        neg_val,l,r = heappop(heap)

        res += -neg_val

        if l+1<=r and (l+1,r) not in vis:
            heappush(heap,(-get_diff(l+1,r),l+1,r))
            vis.add((l+1,r))

        if l<=r-1 and (l,r-1) not in vis:
            heappush(heap,(-get_diff(l,r-1),l,r-1))
            vis.add((l,r-1))

    return res

            



        





        