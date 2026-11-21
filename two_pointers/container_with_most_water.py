"""
Link: https://www.geeksforgeeks.org/problems/container-with-most-water0535/1

Time Complexity: O(n)
- Both pointers move towards each other and visit each element at most once.

Space Complexity: O(1)
- Only a few variables are used.

Concept:
- Start with two pointers at both ends to get the maximum possible width first.
- The water height is always limited by the shorter line, so area = (r - l) * min(arr[l], arr[r]).
- Always move the pointer at the shorter line inward.
- Why: Moving the taller line inward reduces the width while the height stays limited by the same shorter line (or gets even smaller), so area can never increase.
"""

def maxWater(arr):
    l = 0
    r = len(arr) - 1
    area = 0

    while l < r:
        height = min(arr[l], arr[r])
        area = max(area, (r - l) * height)

        # Move the shorter line inward to look for a taller line
        if arr[l] <= arr[r]:
            l += 1
        else:
            r -= 1

    return area