"""
Link: https://leetcode.com/problems/calculate-digit-sum-of-a-string/

Time Complexity: O(n)
- Inner loop (1 round of length L): creates (L / k) groups, each takes O(k) work -> O(L).
- Outer loop (rounds):
  - Each group of k digits has max sum = 9*k -> max digits per group = log (9k).
  - New length after 1 round = (L / k) * log (9k).
- Total work across all rounds = n + n/2 + n/4 + ... = n = O(n).

Space Complexity: O(n)
- 'new_s' list and joined string hold at most O(n) characters in round 1.

Concept:
- Chunk-based string simulation with step 'k' and list-join (''.join()) to avoid O(n^2) string concatenation.
"""

def digitSum(s):
    while len(s) > k:
        new_s = []
        for i in range(0, len(s), k):
            chunk = s[i:i + k]
            chunk_sum = sum(int(ch) for ch in chunk)
            new_s.append(str(chunk_sum))

        s = ''.join(new_s)
    return s