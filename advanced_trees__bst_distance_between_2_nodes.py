# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def lca(self, A, B, C):
        if not A:
            return 0
        #curr=A
        # while curr:       
        #     if B<curr.val and C<curr.val:
        #         curr=curr.left
        #     elif B>curr.val and C>curr.val:
        #         curr=curr.right
        #     else:
        #         return curr
        if B<A.val and C<A.val:
            return self.lca(A.left,B,C)
        if B>A.val and C>A.val:
            return self.lca(A.right,B,C)
        else:
            return A

    def find_dist(self, root, value, dist):
        while root:
            if root.val<value:
                root=root.right
                dist+=1
            elif root.val>value:
                root=root.left
                dist+=1
            else:
                return dist



    def solve(self, A, B, C):

        lca_val=self.lca(A,B,C)
        find_B=self.find_dist(lca_val,B,0)
        find_C=self.find_dist(lca_val,C,0)

        return find_B+find_C

