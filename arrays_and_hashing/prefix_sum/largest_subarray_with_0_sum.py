"""
Link: https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1

Time Complexity: O(n)
- Single pass through the array with O(1) average hash map lookups and insertions.

Space Complexity: O(n)
- Hash map stores at most n distinct prefix sums.

Concept:
- Maintain a running prefix sum and store the earliest index where each prefix sum occurs in a hash map (seeded with {0: -1} to handle zero-sum subarrays starting at index 0).
- If the current prefix sum has been seen before at index j, the subarray from j + 1 to i sums to 0, giving length i - j.
- Only record a prefix sum's first occurrence to maximize subarray length.
"""

def maxLength(arr):
    prev_ps = {0:-1}
    n = len(arr)
    ps = res = 0
    
    for i in range(n):
        
        ps += arr[i]
        
        if ps in prev_ps:
            res = max(res,i-prev_ps[ps])
        else:
            prev_ps[ps] = i
            
    return res