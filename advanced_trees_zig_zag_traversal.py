# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
from collections import deque


class Solution:
	# @param A : root node of tree
	# @return a list of list of integers
###############################2 stack 1927 ms approach#####################
    def zigzagLevelOrder(self, A):
        #edgecase
        if A==None:
            return A
        if A.left==None and A.right == None:
            return A
        
        #variable decleration    
        stack_curr=deque()
        stack_next=deque()
        
        list_output=[]
        
        stack_curr.append(A)
        toggle_level=True
        
        while stack_curr:
            
            size=len(stack_curr)
            row=[]
            for i in range(size):
                x=stack_curr.pop()
                row.append(x.val)
                if toggle_level:
                    if x.left:
                        stack_next.append(x.left)
                    if x.right:
                        stack_next.append(x.right)
                else:
                    if x.right:
                        stack_next.append(x.right)
                    if x.left:
                        stack_next.append(x.left)
                list_output.append(row)
                toggle_level=not toggle_level
                stack_curr,stack_next=stack_next,stack_curr
                
                    
                    
            
        return list_output
    
################################my approach 3741 ms #################################

	# def zigzagLevelOrder(self, A):
    #     if not A:
    #         return []
        
        


    #     stack1=deque()
    #     stack2=deque()

    #     list_output=[]
    #     stack1.append(A)

    #     level=1

    #     while stack1 or stack2:
    #         if level%2!=0:
    #             size=len(stack1)
    #         else:
    #             size=len(stack2)
    #         row=[]
    #         for i in range(size):
    #             if level%2!=0:
    #                 x=stack1.pop()
    #             else:
    #                 x=stack2.pop()
    #             row.append(x.val)
    #             if level%2!=0:
    #                 if x.left:
    #                     stack2.append(x.left)
    #                 if x.right:
    #                     stack2.append(x.right)
    #             else:
    #                 if x.right:
    #                     stack1.append(x.right)
    #                 if x.left:
    #                     stack1.append(x.left)
    #         list_output.append(row)
    #         level+=1
        
    #     return list_output
        
        
     