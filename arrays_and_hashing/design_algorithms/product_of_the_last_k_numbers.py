"""
Link: https://leetcode.com/problems/product-of-the-last-k-numbers/

Time Complexity:
- add(num): O(1) — Appends the running prefix product in constant time.
- getProduct(k): O(1) — Computes the subarray product using two prefix values in constant time.

Space Complexity: O(n)
- Stores one running product entry in the list for each added number.

Concept:
- Maintain a running prefix product list while tracking the index of the most recent zero.
- Why it works:
  - Just like prefix sums find subarray sums via prefix[r] - prefix[l - 1], prefix products find subarray products via prefix[r] // prefix[l - 1].
  - A zero breaks the multiplication chain and turns every future prefix product into 0, so the running product resets to num whenever the previous entry is 0.
  - If the last zero lies inside the last k elements (last_zero_idx >= n - k), the product is immediately 0; otherwise, all elements after that zero form a valid non-zero chain.
"""

class ProductOfNumbers:

    def __init__(self):
        self.stack = []
        self.last_zero_idx = -1
        
    def add(self, num: int) -> None:

        prod = self.stack[-1]*num if self.stack and self.stack[-1]!=0 else num
        self.stack.append(prod)
        if num == 0:
            self.last_zero_idx = len(self.stack) - 1

    def getProduct(self, k: int) -> int:
        n = len(self.stack)
        start_idx = n - k

        if self.last_zero_idx!=-1 and self.last_zero_idx>=start_idx:
            return 0
            
        prev = 1 if start_idx == 0 or self.stack[start_idx-1] == 0 else self.stack[start_idx-1]

        return self.stack[-1]//prev

# Note :     
# ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)