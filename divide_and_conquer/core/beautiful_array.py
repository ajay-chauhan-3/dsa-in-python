'''
link : https://leetcode.com/problems/beautiful-array/?envType=problem-list-v2&envId=dsa-sorting-plateau-divide-and-conquer

time complexity : O(nlogn)

---------------------------

recursion depth = logn
array copy / creation and slice : O(n)
space complexity : O(n)

concept : increase gap between the consecutive numbers

    [1,2,3,4,5,6,7,8] - original array
  [1,3,5,7]   [2,4,6,8] - divide
 [1,5] [3,7] [2,6] [4,8] - divide and combine

'''

def beautifulArray(n):

    nums = [i for i in range(1,n+1)]
    
    def divide(arr):
        n = len(arr)

        if n<=2:
            return arr

        left = divide(arr[::2])
        right = divide(arr[1::2])

        return left + right

    return divide(nums)