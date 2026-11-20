

"""
Link: https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1

Dependency Note:
- Solution 2 uses sortedcontainers (pip install sortedcontainers) to simulate a balanced BST / multiset in Python for O(log n) insertions, deletions, and binary search.

Time Complexity:
- Solution 1 (Merge Sort): O(n log n)
  - Array is recursively split into halves (log n levels) and merged in O(n) time at each level.
- Solution 2 (SortedList): O(n log n)
  - Iterates through n elements, each bisect_right and add operation takes O(log n).

Space Complexity:
- Solution 1: O(n)
  - Temporary arrays during slicing and merging take O(n) auxiliary space, recursion stack takes O(log n).
- Solution 2: O(n)
  - SortedList stores up to n elements.

Concept:
- Count pairs (i, j) where i < j and arr[i] > arr[j] without scanning all pairs.
- Either divide the array via Merge Sort to count cross-inversions while merging sorted halves
- or maintain a sorted structure of seen elements from left to right to count how many prior elements are strictly greater than the current element.
"""

# Solution 1: Merge Sort 
def inversionCount(arr):
    def merge_sort(arr):
        n = len(arr)

        if n <= 1:
            return arr, 0

        mid = n // 2

        left, left_inv = merge_sort(arr[:mid])
        right, right_inv = merge_sort(arr[mid:])

        inv_count = 0
        merged = []

        left_size = len(left)
        right_size = len(right)

        i = j = 0

        while i < left_size and j < right_size:
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inv_count += left_size - i
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged, left_inv + right_inv + inv_count

    return merge_sort(arr)[1]


# Solution 2: SortedList (Binary Search)
from sortedcontainers import SortedList

def inversionCount(self, arr):
    l = SortedList()
    res = 0

    for x in arr:
        j = l.bisect_right(x)
        res += len(l) - j
        l.add(x)

    return res
