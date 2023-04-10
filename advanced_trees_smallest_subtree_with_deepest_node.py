# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def __init__(self):
        self.req_node=TreeNode(None)
        self.maxdepth=-2

    def ht_tree(self,A,depth):
        if not A:
            return depth

        depth_left=self.ht_tree(A.left,depth+1)
        depth_right=self.ht_tree(A.right,depth+1)

        # If the left and right subtrees have the same depth and the depth is
        # greater than or equal to the maximum depth so far,
        # update the reference to the current node and the maximum depth
        # you can use with depth_left or depth_right

        if (depth_left==depth_right) and self.maxdepth<=depth_left:
            self.maxdepth=depth_left
            self.req_node=A

        # Alternative section

        # if (depth_left==depth_right) and self.maxdepth<=depth_right:
        #     self.maxdepth=depth_right
        #     self.req_node=A

        

        return max(depth_left,depth_right)        

        
    def solve(self, A):
        
        self.ht_tree(A,0)

        return self.req_node


