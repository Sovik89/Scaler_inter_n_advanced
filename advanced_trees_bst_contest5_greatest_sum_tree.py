class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def __init__(self):
        self.sum_val=0
        
    def greatest_sum(self,root):
        if not root:
            return
        
        self.greatest_sum(root.right)
        self.sum_val+=root.val
        root.val=self.sum_val
        self.greatest_sum(root.left)
        
        
        
    def solve(self, A):

        self.greatest_sum(A)
        
        return A