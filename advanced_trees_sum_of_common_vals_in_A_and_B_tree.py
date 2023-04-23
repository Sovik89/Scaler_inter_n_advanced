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
    # @param B : root node of tree
    # @return an integer
    #hash_map=dict()

    def __init__(self):
        self.ans=0

    # def inorder(self, root,hash_map):
        
    #     #global hash_map
    #     if not root:
    #         return
    #     self.inorder(root.left,hash_map)
        
    #     if root.val in hash_map:
    #         hash_map[root.val]+=1
    #         self.ans+=root.val
    #     else:
    #         hash_map[root.val]=1
        
    #     self.inorder(root.right,hash_map)
        
    def preorder(self, root,hash_map):
        
        #global hash_map
        if not root:
            return
        
        
        if root.val in hash_map:
            hash_map[root.val]+=1
            self.ans+=root.val
        else:
            hash_map[root.val]=1
        
        self.preorder(root.left,hash_map)
        self.preorder(root.right,hash_map)
                
    
    def solve(self, A, B):
        #global ans
        hash_map=dict()
        mod_val=(10**9)+7

        if not A or not B:
            return 0
        
        self.preorder(A,hash_map)
        self.preorder(B,hash_map)
        
        return self.ans%mod_val
                
                
