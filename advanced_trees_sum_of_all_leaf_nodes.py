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
        if A == None:
            return 0

        left_sum_count=0

        #checking if value is a genuine left leaf node
        if A.left and not A.left.left and not A.left.right:
            left_sum_count+=A.left.val

        #we check all the left leaf node in left and right child
        left_sum_count+=(self.solve(A.left)+self.solve(A.right))


        return left_sum_count






