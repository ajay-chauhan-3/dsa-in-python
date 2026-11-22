"""
Link: https://www.geeksforgeeks.org/problems/peak-element/1

Time Complexity:
- Solution 1 (Binary Search): O(log n)
  - Search space halves at each step by checking the local slope between mid and mid + 1.
- Solution 2 (Linear Scan): O(n)
  - Single pass through the array checking adjacent elements.

Space Complexity:
- Solution 1: O(1)
  - Constant extra pointers used.
- Solution 2: O(1)
  - Constant extra variables used.

Concept:
- Since adjacent elements are distinct and both ends are bounded by negative infinity, at least one peak always exists.
- Either follow the upward slope using binary search in O(log n) or linearly scan each index against its neighbors in O(n).
"""

# Solution 1: Binary Search 

def peakElement(arr):
    low, high = 0, len(arr) - 1

    while low < high:
        mid = (low + high) // 2
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return low

# Solution 2: 

def peakElement(arr):
    n = len(arr)

    if n == 1:
        return 0

    for i in range(0, n):
        if i == 0:
            if arr[i] > arr[i + 1]:
                return i
        elif i == n - 1:
            if arr[i] > arr[i - 1]:
                return i
        elif arr[i - 1] < arr[i] > arr[i + 1]:
            return i