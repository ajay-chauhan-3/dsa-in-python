"""
Link: https://leetcode.com/problems/smallest-unique-subarray/

Time Complexity: O(n log n)
- Precomputing base powers takes O(n) time
- Binary search runs O(log n) iterations, and each check(mid) slides a window across the array in O(n) time.

Space Complexity: O(n)
- Power arrays and the hash_dict frequency map store at most O(n) entries.

Concept:
- Binary search on the subarray length mid, and use a sliding window with double rolling hash to check if any subarray of length mid appears only once.
- Why it works:
  - Monotonic property: If a unique subarray of length L exists, extending it by one element also stays unique, so we can binary search for the minimum valid length.
  - Sliding window with rolling hash: Instead of slicing and comparing subarrays in O(mid) time, rolling hash updates the window hash in O(1) as elements enter and leave.
  - Double hashing: Using two different bases and primes reduces collision risk, ensuring identical hashes represent identical subarrays.
"""

from collections import Counter

def smallestUniqueSubarray(nums):
    n = len(nums)

    mod1, mod2 = 10**9 + 7, 10**9 + 9
    base1, base2 = 100003, 100019 # since 10**5 unique nums possible so base should be > 10**5

    pow1 = [1] * (n + 1)
    pow2 = [1] * (n + 1)
    for i in range(1, n + 1):
        pow1[i] = (pow1[i - 1] * base1) % mod1
        pow2[i] = (pow2[i - 1] * base2) % mod2

    def check(mid):
        i = j = 0
        h1 = h2 = 0
        hash_dict = Counter()

        while j < n:
            # forming the digit with base for each mid size subarray
            h1 = (h1 * base1 + nums[j]) % mod1
            h2 = (h2 * base2 + nums[j]) % mod2

            if j - i + 1 > mid:
                h1 = (h1 - nums[i] * pow1[mid]) % mod1
                h2 = (h2 - nums[i] * pow2[mid]) % mod2
                i += 1

            if j - i + 1 == mid:
                hash_dict[(h1, h2)] += 1

            j += 1

        return 1 in hash_dict.values()

    ans = n
    l, r = 1, n
    while l <= r:
        mid = (l + r) // 2
        if check(mid):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1

    return ans