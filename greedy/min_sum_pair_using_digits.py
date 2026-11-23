"""
Link: https://www.geeksforgeeks.org/problems/minimum-sum4058/1

Time Complexity: O(n log n)
- Sorting takes O(n log n) time, and digit-by-digit addition takes O(n) time.

Space Complexity: O(n)
- Splitting into two digit lists and storing result digits takes O(n) space.

Concept:
- Sort digits in ascending order and distribute them alternately into two numbers, then add from right to left.
- Why it works:
  - Higher place values (100s, 10s) carry much larger weights than lower ones (1s), so smaller digits must go to higher place values first.
  - At any specific place value level (e.g., 10s place), both digits get multiplied by the same power of 10 (10 * (d1 + d2)).
  - Because addition is commutative, swapping which number gets d1 vs d2 within the same place value produces the exact same sum.
"""

def minSum(arr):
    n = len(arr)
    arr.sort()
    
    arr1 = arr[::2]
    arr2 = arr[1::2]
    
    if len(arr1)>len(arr2):
        arr2 = [0]+arr2
    
    res = []   
    carry = 0
    for d1,d2 in zip(reversed(arr1),reversed(arr2)):
        carry,digit = divmod(d1+d2+carry,10)
        res.append(str(digit))
        
    if carry:
        res.append(str(carry))
        
    ans = ''.join(reversed(res)).lstrip('0')
        
    return ans if ans else '0'
            