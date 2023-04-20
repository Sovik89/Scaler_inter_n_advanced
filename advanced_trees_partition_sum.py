# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
import sys
sys.setrecursionlimit(10**6)

class Solution:
    # @param A : root node of tree
    # @return an integer
    def __init__(self):
        self.sum_set=set()  
    
    
    def solve(self, A):
               
        def check_sum(root):
            if not root:
                return 0
            
            sum_val=root.val+self.check_sum(root.left)+self.check_sum(root.right)
            self.sum_set.add(sum_val)
            
            return sum_val
        
        
        total_val=check_sum(A)
        
        if total_val//2 in self.sum_set:
            return 1
        
        return 0