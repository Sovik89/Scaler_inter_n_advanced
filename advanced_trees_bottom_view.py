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
        hash_map = dict()
        my_queue = deque()
        my_queue.append((A, 0))
        
        
        while my_queue :
            popped_pair = my_queue.popleft()
            
           
            if popped_pair[1] not in hash_map :
                hash_map[popped_pair[1]] = [popped_pair[0].val]
            else :
                hash_map[popped_pair[1]].append(popped_pair[0].val)

            # min_key = min(min_key, popped_pair[1])
            # max_key = max(max_key,popped_pair[1])

            if popped_pair[0].left :
                my_queue.append((popped_pair[0].left, popped_pair[1] - 1))
            if popped_pair[0].right :
                my_queue.append((popped_pair[0].right, popped_pair[1] + 1))

        min_key=min(hash_map)
        max_key=max(hash_map)

        ans = []
        for i in range(min_key, max_key + 1) :
            #ans.append(hash_map[i])
            #last value or bottom view
            top_val=hash_map[i][-1]
            ans.append(top_val)
        
        return ans