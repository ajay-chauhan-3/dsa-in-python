"""
Link: https://www.geeksforgeeks.org/problems/maximum-index-1587115620/1

Time Complexity: O(n)
- Building max_idx from right to left takes O(n) time, and both pointers i and j move forward at most n steps.

Space Complexity: O(n)
- The max_idx array takes O(n) space to store suffix maximum indices.

Concept:
- Traverse from the end (right to left) to build max_idx, where max_idx[i] stores the index of the maximum element in the suffix arr[i..n-1], then use two pointers i and j to find the widest valid gap.
- Why it works:
  - Keeping max from right: For any left index i, if a larger element exists further right, picking an earlier smaller element is never optimal. max_idx[j] jumps straight to the furthest valid right candidate.
  - Jumping j to max_idx[j] + 1: Everything between j and max_idx[j] is smaller than or equal to arr[max_idx[j]], so once max_idx[j] is checked, intermediate indices cannot give a better answer for i and can be safely skipped.
  - Moving i forward: When cur_min > arr[max_idx[j]], no element from j onward is large enough for the current cur_min, so i moves right to look for a smaller cur_min while j stays where it stopped.
"""


def maxIndexDiff(arr):
    n = len(arr)
    
    max_idx = [n-1]*n
    
    #  build max_arry from right (saving indexes)
    for i in range(n-2,-1,-1):
        if arr[i]>arr[max_idx[i+1]]:
            max_idx[i] = i
        else:
            max_idx[i] = max_idx[i+1]
            
    cur_min = arr[0]
    i = j = 0
    res = 0

    while i<n:
        cur_min = min(cur_min,arr[i])
        
        while j<n and cur_min <= arr[max_idx[j]]:
            res = max(res,max_idx[j]-i)
            j = max_idx[j]+1
            
        i += 1
            
    return res
                
                