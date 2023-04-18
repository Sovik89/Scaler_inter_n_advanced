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
    # @param B : integer
    # @param C : integer
    # @return an integer
    def inorder(self,root,arr):
        if not root:
            return
        self.inorder(root.left,arr)
        arr.append(root.val)
        self.inorder(root.right,arr)

    def solve(self, A, B, C):

        list_val=[]

        self.inorder(A,list_val)

        n=len(list_val)
        count=0
        for i in range(n):
            if B<=list_val[i]<=C:
                count+=1
        
        return count

