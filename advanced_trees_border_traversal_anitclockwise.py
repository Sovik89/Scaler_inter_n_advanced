# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
from collections import deque

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def leaf(self,A):
        ans=[]
        stack=deque()
        stack.append(A)
        while stack:
            x=stack.pop()
            if not x.left and not x.right:
                ans.append(x.val)
            if x.right:
                stack.append(x.right)
            if x.left:
                stack.append(x.left)

        return ans


    def leftborder(self,A):
        ans=[]

        while A:
            if A.left or A.right:
                ans.append(A.val)
            if A.left:
                A=A.left
            else:
                A=A.right

        return ans

    def rightborder(self,A):
        ans=[]

        while A:
            if A.left or A.right:
                ans.append(A.val)
            if A.right:
                A=A.right
            else:
                A=A.left

        return ans

    def solve(self, A):
        left=self.leftborder(A)
        mid=self.leaf(A)
        right=self.rightborder(A)

        right=right[1:]#root is taken by the leftborder

        final=left+mid+right[::-1]

        return final
    
    
    
    ############Explaination###############
    
"""
The solution involves three helper functions - leaf, leftbound, and rightbound,
and a main function solve.

The leaf function returns a list of values of all the leaf nodes of the binary tree,
which are the nodes without any child. It uses a stack to traverse the tree
and appends the value of a node to the list ans if it has no left or right child.

The leftbound function returns a list of values of the left boundary of the binary tree.
It traverses the binary tree from the root node to the left-most node,
appending the value of each node to the list ans if it has a child in the left subtree.
If a node does not have a left child, it goes to its right child.

The rightbound function is similar to leftbound but returns a list of values of the
right boundary of the binary tree.

The solve function calls the leftbound, rightbound, and leaf functions
to get the left boundary,right boundary, and leaf nodes of the binary tree, respectively.
It then removes the first element of the right boundary list as it is the same as the root node,
and combines the lists left, final, and right[::-1] to get the
final list of boundary values in anti-clockwise direction starting from the root.

"""    