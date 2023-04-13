# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return the root node in the tree
    def buildTree(self, A, B):
        if not A or not B:
            return None
        
        root=TreeNode(A[0])

        root_index=B.index(A[0])

        root.left=self.buildTree(A[1:root_index+1],B[:root_index])
        root.right=self.buildTree(A[root_index+1:],B[root_index+1:])

        return root
    
    
# To construct a binary tree given its preorder and inorder traversals,
#     we can follow the following recursive approach:

#     1. The first element in the preorder traversal is the root of the binary tree.
#     2. Search for the position of the root in the inorder traversal to determine the left and 
#     right subtrees.
#     3. The elements to the left of the root in the inorder traversal form the left subtree,
# and the elements to the right of the root in the inorder traversal form the right subtree.
#     4. Recursively construct the left subtree using the left part of the inorder traversal
# and the left part of the preorder traversal.
#     5. Recursively construct the right subtree using the right part of the inorder traversal
# and the right part of the preorder traversal.
#     6. Return the root of the constructed binary tree.