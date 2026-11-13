"""
Link: https://leetcode.com/problems/beautiful-array/

Time Complexity: O(n log n) # logn levels and each level doing linear work O(n)
Space Complexity: O(n)  # recursion depth: O(log n), array slicing/creation: O(n)

Concept:
- Recursively split alternate elements (arr[::2] and arr[1::2]) to keep doubling the gap between consecutive numbers
- Increasing the gap at every level ensures no two outer elements can average out to an element between them (A[i] + A[j] != 2 * A[k])
- Combine left and right halves once divided down to single or double elements

Dry Run:
       [1, 2, 3, 4, 5, 6, 7, 8]    <- gap = 1
      [1, 3, 5, 7]   [2, 4, 6, 8]  <- gap = 2
     [1, 5]  [3, 7] [2, 6]  [4, 8] <- gap = 4
"""

def beautifulArray(n):

    nums = [i for i in range(1,n+1)]
    
    def divide(arr):
        n = len(arr)

        if n<=2:
            return arr

        left = divide(arr[::2])
        right = divide(arr[1::2])

        return left + right

    return divide(nums)