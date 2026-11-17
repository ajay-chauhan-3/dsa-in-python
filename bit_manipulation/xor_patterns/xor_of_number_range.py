"""
Link: https://www.geeksforgeeks.org/problems/find-xor-of-numbers-from-l-to-r/1

Time Complexity: O(1)
- Constant time modulo and XOR operations.

Space Complexity: O(1)
- No extra memory used.

Concept:
- Use prefix XOR: XOR(l to r) = XOR(0 to r) ^ XOR(0 to l - 1), since common elements in [0 .. l-1] cancel out (a ^ a = 0).
- Every consecutive (even, odd) pair differs only in the last bit, so (2k) ^ (2k + 1) = 1.
- Because of this, every complete group of 4 numbers (4k .. 4k+3) XORs to 1 ^ 1 = 0, making XOR(0 to x) repeat in a simple cycle of 4 based on x % 4:
  - x % 4 == 0 -> x
  - x % 4 == 1 -> 1
  - x % 4 == 2 -> x + 1
  - x % 4 == 3 -> 0
"""

def findXOR(l,r):
    # code here
    def dfs(x):
        rem = x%4
        if rem == 0:
            return x
        elif rem == 1:
            return 1
        elif rem == 2:
            return x+1
        else:
            return 0
            
    return dfs(r) ^ dfs(l-1)