# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
from collections import deque

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        sum_odd=0
        sum_even=0
        my_queue=deque()

        my_queue.append(A)
        level=1

        while len(my_queue)>0:
            size=len(my_queue)
            
            sum_val=0
            for i in range(size):
                temp=my_queue.popleft()
                sum_val+=temp.val
                if temp.left:
                    my_queue.append(temp.left)
                if temp.right:
                    my_queue.append(temp.right)
            if level%2==0:
                sum_even+=sum_val
            else:
                sum_odd+=sum_val
            level+=1

            
        
        return sum_odd-sum_even

        
