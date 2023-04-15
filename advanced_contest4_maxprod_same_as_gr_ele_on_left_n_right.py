from collections import deque

def maxSpecialProduct(A):
    n=len(A)
    
    #Initializing the left special value aned the right special value
    LSV=[0]*n
    RSV=[0]*n
    mod=(10**9)+7
    #determine the left special value array
    stacks=deque()
    
    
    for i in range(n):
        while stacks and A[stacks[-1]]<=A[i]:
            stacks.pop()
            
        if stacks:
            LSV[i]=stacks[-1]
        stacks.append(i)

    #determine the right special value array
    stacks=deque()
    
    for i in range(n-1,-1,-1):
        while stacks and A[stacks[-1]]<=A[i]:
            stacks.pop()
            
        if stacks:
            RSV[i]=stacks[-1]
        stacks.append(i)
        
    max_val=0
    for i in range(n):
        value=LSV[i]*RSV[i]
        
        if value>0:
            max_val=max(value,max_val)
            
    
    return max_val%mod



print(maxSpecialProduct([8,2,7,4,9,10]))