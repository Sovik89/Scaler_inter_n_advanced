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

        n=len(B)-1

        root_val=B[n]

        root=TreeNode(B[n])

        #inorder position

        root_index=A.index(B[n])

        root.left=self.buildTree(A[:root_index],B[:root_index])
        root.right=self.buildTree(A[root_index+1:],B[root_index:n])

        return root
    
    
        """
        Here's a brief explanation of how it works:

        The postorder traversal gives us the root node of the tree as the last element in the list.
        We can create a TreeNode object with this value.

        Next, we find the index of this root node value in the inorder traversal.
        This index gives us the left and right subtrees of the root node.

        Using the left and right subtrees, we can recursively construct the left and right children of the root node.
        The left subtree will be constructed from the portion of the inorder and postorder traversal lists
        that comes before the index of the root node in the inorder traversal.
        Similarly, the right subtree will be constructed from the portion of the inorder and postorder traversal lists
        that comes after the index of the root node in the inorder traversal.

        Finally, we return the root node of the binary tree.

        """