"""
Link: https://www.geeksforgeeks.org/problems/sort-in-specific-order2422/1

Time Complexity: O(n log n)
- Python's Timsort performs O(n log n) comparisons, with an O(1) tuple key lookup per element.

Space Complexity: O(n)
- Timsort uses up to O(n) auxiliary space in the worst case (in-place modification of input array).

Concept:
- Custom tuple-based sorting:
  - Python compares tuples element-by-element from left to right.
  - First key x % 2 == 0 evaluates to False (0) for odd numbers and True (1) for even numbers, placing all odd numbers before even numbers.
  - Second key -x if x % 2 else x sorts odd numbers in descending order (using negation) and even numbers in ascending order.
"""


def sortIt(arr):
    arr.sort(key=lambda x: (x % 2 == 0, -x if x % 2 else x))