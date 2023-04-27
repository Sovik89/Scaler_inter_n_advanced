# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

import sys
sys.setrecursionlimit(10**6)

class Solution:
    # @param root, a tree node
    # @return nothing
    def first_node_in_next_level(self,root):
        if not root:
            return
        if root.left:
            return root.left
        if root.right:
            return root.right
        return self.first_node_in_next_level(root.next)

    def connect(self, root):
        while root:
            node= root
            
            while node:
                if node.left:
                    if node.right:
                        node.left.next=node.right
                    else:
                        node.left.next=self.first_node_in_next_level(node.next)
                if node.right:
                    node.right.next=self.first_node_in_next_level(node.next)
                node=node.next

            root=self.first_node_in_next_level(root)