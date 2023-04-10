from collections import deque

def prevSmaller(A):

    ########################O(N**2)#############################
    # n=len(A)
    # ans=[-1]*n
        
    # for i in range(1,n):

    #     for j in range(i-1,-1,-1):
    #         if A[j]<A[i]:
    #             ans[i]=A[j]
    #             break
            
            
    # return ans

    n=len(A)
    ans=[-1]*n
    
    stacks=deque()
    
    for i in range(n):
        while stacks and stacks[-1]>=A[i]:
            stacks.pop()
        if stacks:
            ans[i]=stacks[-1]
        stacks.append(A[i])
        
    return ans


print(prevSmaller([ 34, 35, 27, 42, 5, 28, 39, 20, 28 ]))