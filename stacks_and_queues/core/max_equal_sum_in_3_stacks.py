"""
Link: https://www.geeksforgeeks.org/problems/find-maximum-equal-sum-of-three-stacks/1

Time Complexity: O(n1 + n2 + n3)  # at least one element is popped per iteration
Space Complexity: O(1)            # only tracking running sums and pointers

Concept:
- Greedy elimination: repeatedly pop the top element from the stack(s) having the current maximum sum until all three sums become equal
"""

def maxEqualSum(s1, s2, s3):
    
    i = j = k = 0
    n1,n2,n3 = len(s1),len(s2),len(s3)
    
    s1_total,s2_total,s3_total = sum(s1),sum(s2),sum(s3)
    
    if s1_total == s2_total == s3_total:
        return s1_total
    
    while i<n1 and j<n2 and k<n3:
            
        curr_max = max(s1_total,s2_total,s3_total)
        
        if curr_max == s1_total:
            s1_total -= s1[i]
            i+=1
            
        if curr_max == s2_total:
            s2_total -= s2[j]
            j+=1
            
        if curr_max == s3_total:
            s3_total -= s3[k]
            k+=1
            
        if s1_total == s2_total == s3_total:
            return s1_total
    
    return 0