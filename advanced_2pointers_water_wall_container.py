def maxArea(A):
    """
    Given n non-negative integers A[0], A[1], ..., A[n-1] , where each represents a point at coordinate (i, A[i]).

    N vertical lines are drawn such that the two endpoints of line i is at (i, A[i]) and (i, 0).

    Find two lines, which together with x-axis forms a container, such that the container contains the most water.

    Note: You may not slant the container.
    """
    #brute force
    
    # n=len(A)
    
    # ans=0
    # for i in range(n):
    #     for j in range(1,n):
    #         h=min(A[i],A[j])
    #         length=j-i
    #         ans=max(ans,h*length)
    
    # return ans
    
    #2 pointer
    
    n=len(A)
    
    p1=0
    p2=n-1
    ans=0
    while p1<p2:
        h=min(A[p1],A[p2])
        length=p2-p1
        val=h*length
        
        ans=max(ans,val)
        if A[p1]>A[p2]:
            p2-=1
        else:
            p1+=1
        
    return ans

print(maxArea([1, 5, 4, 3]))
print(maxArea([1]))
            
            