# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
from collections import deque


class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root:
            return root
        
        my_queue=deque()
        
        my_queue.append(root)
        
        while len(my_queue)>0:
            size=len(my_queue)
            
            for i in range(size):
                
                x=my_queue.popleft()
                
                if x.left:
                    my_queue.append(x.left)
                    
                if x.right:
                    my_queue.append(x.right)
                    
            for j in range(1,len(my_queue)):
                my_queue[j-1].next=my_queue[j]
        

        
