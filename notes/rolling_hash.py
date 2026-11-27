"""
Link: https://leetcode.com/problems/smallest-unique-subarray/

================================================================================
LEARNING NOTES: ROLLING HASH IN SIMPLE WORDS
================================================================================

1. HOW NUMBERS ARE FORMED (BASE SYSTEM)
--------------------------------------------------------------------------------
- Every number system builds a single number from digits using powers of a Base:
  - Base 10 (digits 0 to 9): 452 = 4*(10^2) + 5*(10^1) + 2*(10^0)
  - Base 2  (digits 0 to 1): 101 = 1*(2^2)  + 0*(2^1)  + 1*(2^0) = 5
  - Base 8  (digits 0 to 7): 37  = 3*(8^1)  + 7*(8^0)  = 31
- In the same way, we turn any subarray [a, b, c] into one single number using Base B:
  - Hash([a, b, c]) = (a * B^2 + b * B^1 + c * B^0) % mod
- Why Base B must be bigger than max(nums[i]) (here > 10^5):
  - In Base 10, every digit must be smaller than 10 (0 to 9).
  - If you put "15" in one place in Base 10, 10 spills over into the next place (1*10 + 15 = 25, which equals [2, 5] = 2*10 + 5 = 25).
  - Since nums[i] can go up to 10^5, we pick Base > 10^5 (100003) so two different subarrays never mix up like that.


2. WHY NORMAL HASHING IS SLOW & HOW ROLLING HASH WORKS IN O(1)
--------------------------------------------------------------------------------
- Normal Hashing (tuple(nums[i:j+1])):
  - Reads all mid elements at every step -> O(n * mid) time -> 5 * 10^9 ops for n = 10^5 -> TLE.
- Rolling Hash:
  - Reuses the old window hash in 2 simple O(1) math steps.
- Example (using Base 10 for clarity, arr = [4, 5, 2, 9], mid = 3):
  - First window [4, 5, 2]:
    - h = 4*(10^2) + 5*(10^1) + 2*(10^0) = 452
  - Slide one step right to [5, 2, 9]:
    - Step 1 (Add right number 9): h = 452 * 10 + 9 = 4529 (4 is now at 10^3).
    - Step 2 (Remove left number 4): h = 4529 - 4 * (10^3) = 529 -> Exact hash of [5, 2, 9] in O(1)!

3. WHY SAVE POWERS IN AN ARRAY (pow1, pow2)?
--------------------------------------------------------------------------------
- Every window slide needs base^mid % mod to remove the left number.
- Calculating base^mid again and again inside the loop wastes time.
- Precomputing pow[k] = (base^k) % mod once in O(n) gives O(1) list lookup inside the loop.


4. WHY PRIME BASE, PRIME MOD, AND DOUBLE HASH?
--------------------------------------------------------------------------------
A. Why Prime Mod (and big ~10^9, not 10^5 + 2):
   - Stops terms from turning 0: If base = 10 and mod = 10^5, then 10^5 % 10^5 = 0. In [a,b,c,d,e,f], 'a' gets multiplied by 0 and disappears ([1,2,3,4,5,6] == [9,2,3,4,5,6]).
   - Uses all remainders evenly: If base = 6 and mod = 100002 (6 * 16667), 6^k % 100002 is always a multiple of 6, leaving 5/6th of remainders unused.
   - Big mod (~10^9) avoids easy clashes across 10^5 subarrays.

B. Why Prime Base (100003 instead of 100000):
   - Composite 100000 has small factors (2, 5, 10...) that mix with patterns in input numbers and create repeating remainder cycles.
   - Prime 100003 has no small factors, spreading remainders evenly.

C. Why Double Hash (Birthday Paradox & Probability Math):
   - Think of mod as a dice with M sides (remainders 0 to M - 1):
     - Chance of 2 random subarrays getting the exact same remainder = 1 / M.
   - Why 10^5 subarrays create huge clash chances (Birthday Paradox):
     - Every subarray is checked against all other subarrays in the map.
     - For k = 10^5 subarrays, total pairs compared = k * (k - 1) / 2 ≈ (10^5)^2 / 2 = 5 * 10^9 pairs.
   - Single Hash (mod1 ≈ 10^9):
     - Clash chance per pair = 1 / 10^9.
     - Expected clashes in 1 test case = (5 * 10^9 pairs) * (1 / 10^9) = 5 clashes -> High risk of Wrong Answer!
   - Double Hash (mod1 * mod2 ≈ 10^18):
     - Both h1 AND h2 must match by luck at the exact same time.
     - Clash chance per pair = (1 / 10^9) * (1 / 10^9) = 1 / 10^18.
     - Expected clashes in 1 test case = (5 * 10^9 pairs) * (1 / 10^18) = 5 / 10^9 ≈ 0 (1 clash in ~200 million runs).
================================================================================
"""