
'''
Link : https://leetcode.com/problems/reverse-pairs/

Time Complexity : O(nlogn) # logn levels and each level doing linear work O(n)
Space Complexity: O(n)  # array slicing /while loops - O(n) and recusrion stack - logn

concept:
- divide array till one element
- calculate reverse pairs just before merging left and right array
- merge them in sorted form 
'''

def reversePairs(nums):
    
    def merge_sort(arr):
        n = len(arr)

        if n<=1:
            return arr,0

        mid = n//2

        left,left_reverse_count = merge_sort(arr[:mid])
        right,right_reverse_count = merge_sort(arr[mid:])

        left_size = len(left)
        right_size = len(right)

        i = reverse_count = 0
        
        for right_val in right:                         # O(n)
            while i<left_size and left[i]<=2*right_val:
                i+=1
            reverse_count += left_size - i

        i = j = 0
        merge = []
        
        while i<left_size and j<right_size:             # O(n)

            if left[i]<=right[j]:
                merge.append(left[i])
                i+=1
            else:
                merge.append(right[j])
                j+=1

        merge.extend(left[i:])
        merge.extend(right[j:])

        return merge,left_reverse_count+right_reverse_count+reverse_count
        
    return merge_sort(nums)[1]
