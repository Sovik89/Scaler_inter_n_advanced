# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
from collections import deque

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        my_queue=deque()

        my_queue.append(A)
        list_level=[]

        while len(my_queue)>0:
            size=len(my_queue)
            
            
            for i in range(size):
                temp=my_queue.popleft()
                if i==0:
                    list_level.append(temp.val)
                if temp.left:
                    my_queue.append(temp.left)
                if temp.right:
                    my_queue.append(temp.right)
            #list_level.append(row)
            
        
        return list_level
