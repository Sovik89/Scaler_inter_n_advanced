# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def __init__(self) -> None:
        self.resultant_diameter=0
    
    def diameter(self,A):
        if not A:
            return 0
        lh=self.diameter(A.left)
        rh=self.diameter(A.right)
        
        curr_diameter=lh+rh
        self.resultant_diameter=max(self.resultant_diameter,curr_diameter)
        
        return max(lh,rh)+1
    
    def solve(self, A):
        if not A:
            return 0       
        
        dummy=self.diameter(A)                
        return self.resultant_diameter
