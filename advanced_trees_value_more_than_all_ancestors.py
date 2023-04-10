# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        self.count=0

        def dfs(A,max_val):            
            if A == None:
                return
            if A.val > max_val:
                self.count+=1
            
            max_val=max(A.val,max_val)

            dfs(A.left,max_val)
            dfs(A.right,max_val)
        
        dfs(A,float('-inf'))

        return self.count
