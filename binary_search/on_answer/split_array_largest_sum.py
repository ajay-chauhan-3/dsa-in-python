"""
Link: 
https://leetcode.com/problems/split-array-largest-sum/
https://www.geeksforgeeks.org/problems/split-array-largest-sum--141634/1

Time Complexity: O(n * log(sum(arr) - max(arr)))
- The binary search runs on the answer range from max(arr) to sum(arr), which takes O(log(sum(arr) - max(arr))) steps.
- In each step, we loop through the array once to count required subarrays, taking O(n) time.

Space Complexity: O(1)
- Only a few variables are used.

Concept:
- Use binary search on the answer range from max(arr) to sum(arr).
- For a candidate answer mid, greedily pack as many numbers as possible into each subarray without exceeding mid.
- Why it works: If we need at most k subarrays, mid is valid because any subarray can be split further into smaller pieces to make exact k subarrays without increasing the max sum.
- When mid is valid, try a smaller value, otherwise, increase mid.
"""


def splitArray(arr, k):
    
    n = len(arr)
    
    l = max(arr) # min sum possible
    r = sum(arr) # max sum possible
    
    def check(mid):
        
        arr_count = 1
        cur_sum = 0
        
        for x in arr:
            if cur_sum+x>mid:
                arr_count+=1
                cur_sum=x
                if arr_count>k:
                    return False
            else:
                cur_sum+=x
        return True
    
    ans = r
    
    while l<=r:
        mid = (l+r)//2
        
        if check(mid):
            ans = mid
            r = mid-1
        else:
            l = mid + 1
            
    return ans
            
            
            
            