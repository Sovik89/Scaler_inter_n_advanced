# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @param C : integer
	# @return an integer
    def find_path(self, root,k):
            if root == None:
                return []
            
            if k == root.val:                
                return [root.val]
            
            #find k in root's left subtree
            left_search=self.find_path(root.left,k)
            # If k is found in root's left subtree, 
            # prepend root's value to the list of nodes leading to k and return the list
            if left_search:
                return [root.val]+left_search
            
            #find k in root's right subtree
            right_search=self.find_path(root.right,k)            
            # If k is found in root's right subtree, 
            # prepend root's value to the list of nodes leading to k and return the list
            if right_search:   
                return [root.val]+right_search
            # If k is not found in root or its subtrees, return an empty list
            return []
        
        
    def lca(self, A, B, C):
        path_B=self.find_path(A,B)
        path_C=self.find_path(A,C)
        
        if not path_B or not path_C:
            return -1
        
        i=0
        
        while i<len(path_B) and i<len(path_C) and path_B[i]==path_C[i]:
            i+=1 
        if path_C[i-1]==path_B[i-1]:
            return path_C[i-1]
        
        return -1
            
        
                    
            
        
     
