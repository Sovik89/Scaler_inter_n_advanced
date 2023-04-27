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
    # def solve(self, A):
    #     is_sum_binary_tree=1
        
        
    #     def sum_binary_tree(root):
            
    #         if not root:
    #             return 0
            
    #         if not root.left and not root.right:
    #             return root.val

    #         nonlocal is_sum_binary_tree
            
    #         left_check=sum_binary_tree(root.left)
    #         right_check=sum_binary_tree(root.right)
            
    #         if left_check+right_check!=root.val:
    #             is_sum_binary_tree=0
                
            
    #         return root.val+left_check+right_check
        
    #     dummy=sum_binary_tree(A)#since the dummy value has got nothing to do with any thing
        
    #     return is_sum_binary_tree
    
