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
    # @param B : root node of tree
    # @return an integer
    
    def is_equal(self, A, B):
        if not A and not B:
            return True
        if not A or not B:
            return False
        
        if A.val == B.val:
            return True
        return False
    
    def check_min_swaps(self, A, B):
        ans=0
        
        if self.is_equal(A.left,B.left) and self.is_equal(A.right,B.right):
            value=0
            if A.left:
                value=self.check_min_swaps(A.left,B.left)
            if value==-1:
                return -1
            ans+=value
            value=0

            if A.right:
                value=self.check_min_swaps(A.right,B.right)
            if value==-1:
                return -1
            ans+=value
            
        elif self.is_equal(A.left,B.right) and self.is_equal(A.right,B.left):
            value=0
            ans+=1
            if A.left:
                value=self.check_min_swaps(A.left,B.right)
            if value==-1:
                return -1
            ans+=value
            value=0

            if A.right:
                value=self.check_min_swaps(A.right,B.left)
            if value==-1:
                return -1
            ans+=value
        else:
            return -1
        
        return ans
                
            
        
    def solve(self, A, B):
        if not self.is_equal(A,B):
            return -1
        
        return self.check_min_swaps(A,B)
        