from collections import deque

class Solution:
    # @param A : list of integers
    # @return an integer
    
    
    def solve(self, A):
        n=len(A)
        LSV=[-1]*n
        RSV=[-1]*n
        
        left_stack=deque()
        right_stack=deque()
        
        for i in range(n):
            while left_stack and left_stack[-1]<=A[i]:
                left_stack.pop()
            if left_stack:
                LSV[i]=left_stack[-1]
            left_stack.append(A[i])
            
        
        for j in range(n-1,-1,-1):    
            while right_stack and right_stack[-1]<=A[j]:
                right_stack.pop()
            if right_stack:
                RSV[j]=right_stack[-1]
            right_stack.append(A[j])
            
        count=0
        
        for i in range(n):
            if LSV[i]!=-1:
                count+=1
            if RSV[i]!=-1:
                count+=1
            
            
                
        return count
        
        
        
        
        
        
