"""
Link: https://www.geeksforgeeks.org/problems/k-th-missing-element-in-natural-numbers/1

Time Complexity: O(n log n)  # sorting the array + single pass through 'n' elements
Space Complexity: O(1)       # in-place sort, no extra memory used

Concept:
- Without any removals, the k-th smallest natural number is simply `k`.
- Every removed number `<= k` shifts the target answer 1 step forward (`k += 1`).
- Sorting is required because shifting `k` forward can bring larger removed numbers into the `<= k` range.
"""


def findKthSmall(arr, k):
    arr.sort()

    for x in arr:
        if x <= k:
            k += 1
        else:
            break

    return k