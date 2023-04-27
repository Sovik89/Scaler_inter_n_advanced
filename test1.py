
class Solution:
    
    def __init__(self):
        self.max_val=float('-inf')    
    
    def max_value(self,root):
        if not root:
            return 0
        
        if root.val> self.max_val:
            self.max_val=root.val
            
        self.max_value(root.left)
        self.max_value(root.right)
            
    
    
    def solve(self, A):
        self.max_value(A)
        return self.max_val
        

