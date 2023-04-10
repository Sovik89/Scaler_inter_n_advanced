##########################INORDER###########################

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
    def traverse_in(self,root,arr):
        if root == None:
            return
        self.traverse_in(root.left,arr)
        arr.append(root.val)
        self.traverse_in(root.right,arr)
        
    def inorderTraversal(self, A):
        list_val=[]
        self.traverse_in(A,list_val)
        return list_val
    
    
############################PREORDER#############################

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
    def traverse_pre(self,root,arr):
        if root == None:
            return 
        
        arr.append(root.val)
        self.traverse_pre(root.left,arr)
        self.traverse_pre(root.right,arr)
    
    def preorderTraversal(self, A):
        list_val=[]
        self.traverse_pre(A,list_val)
        return list_val
    
    
#############################POSTORDER###############################


# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
    def traverse_post(self, root, arr):
        if root == None:
            return
        
        self.traverse_post(root.left,arr)
        self.traverse_post(root.right,arr)
        arr.append(root.val)

    def postorderTraversal(self, A):
        list_val=[]
        self.traverse_post(A,list_val)

        return list_val