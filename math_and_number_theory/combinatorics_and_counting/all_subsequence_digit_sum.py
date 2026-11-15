"""
Link: https://www.geeksforgeeks.org/problems/sum-of-all-sub-sequences-of-a-number3437/1

Time Complexity: O(n)   # O(n) to sum all digits + O(log n) for modular exponentiation pow(2, n-1, mod)
Space Complexity: O(1)  # only a few variables used

Concept:
- Contribution Technique (Counting per element instead of per subsequence):
  - If we fix any single digit `s[i]` to be included, the remaining `n - 1` characters each have 2 choices (pick or not pick).
  - So every individual digit `s[i]` appears in exactly `2^(n - 1)` subsequences.
- Why doesn't counting `2^(n - 1)` for every digit cause duplicate sums?
  - A subsequence like "12" is visited twice: once when counting for '1' and once when counting for '2'.
  - During '1's count, it only contributes its '1' to the total sum. During '2's count, it only contributes its '2'.
  - Every digit inside a shared subsequence contributes only its own value, so nothing is double-counted.
- Total Sum = (sum of all digits) * 2^(n - 1).
"""

def subsequenceSum(s):
    mod = 10**9 + 7
    n = len(s)

    half = pow(2, n - 1, mod)  # O(log n) fast modular exponentiation

    digit_sum = 0
    for x in s:
        digit_sum = (digit_sum + int(x)) % mod

    return (digit_sum * half) % mod