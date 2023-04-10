from collections import deque

def nextGreater(A):
    n=len(A)
    ans=[-1]*n
    
    stacks=deque()
    
    for i in range(n-1,-1,-1):
        while stacks and stacks[-1]<=A[i]:
            stacks.pop()
        if stacks:
            ans[i]=stacks[-1]
        stacks.append(A[i])
        
    return ans

print(nextGreater([ 34, 35, 27, 42, 5, 28, 39, 20, 28 ]))