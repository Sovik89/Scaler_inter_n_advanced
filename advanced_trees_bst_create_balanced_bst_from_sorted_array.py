# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    
    def createBBST(self, A, s, e):
        if s>e:
            return
        
        mid=(s+e)//2
        
        root=TreeNode(A[mid])
        
        root.left=self.createBBST(A,s,mid-1)
        root.right=self.createBBST(A,mid+1,e)
        
        return root
    
    
    def sortedArrayToBST(self, A):
        
        return self.createBBST(A, 0, len(A)-1)
                    
                    
                