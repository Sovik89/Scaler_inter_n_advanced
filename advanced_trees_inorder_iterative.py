# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
from collections import deque

class Solution:
	# @param A : root node of tree
	# @return a list of integers
    def inorderTraversal(self, A):
        stack=deque()
        curr=A
        list_inorder=[]
        while True:
            if curr:
                stack.append(curr)
                curr=curr.left
            elif stack:
                curr=stack.pop()
                list_inorder.append(curr.val)
                curr=curr.right
            else:
                break

        return list_inorder