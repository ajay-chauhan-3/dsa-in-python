"""
Link: https://www.geeksforgeeks.org/problems/count-pairs-in-an-array4145/1

Dependency Note:
- uses sortedcontainers (pip install sortedcontainers) to simulate a balanced BST / multiset in Python for O(log n) insertions, deletions, and binary search.

Time Complexity: O(n log n)
- loop through n elements, and each binary search (bisect_left) and insertion in SortedList takes O(log n) time.

Space Complexity: O(n)
- The SortedList stores up to n values.

Concept:
- Transform each element into val[i] = i * arr[i], which turns the problem into counting inversions (pairs where i < j and val[i] > val[j]).
- Keep a sorted list of all val[i] seen so far as we move from left to right.
- For each new value, use binary search to count how many previous values are strictly greater than it.
- Why it works: Every previous value in the list has a smaller index, so any value greater than the current one forms a valid pair.
"""

from sortedcontainers import SortedList

def countPairs(arr):
    n = len(arr)
    res = 0
    l = SortedList([0])

    for i in range(1, n):
        x = arr[i]
        j = l.bisect_left(i * x + 1)
        res += len(l) - j
        l.add(i * x)

    return res