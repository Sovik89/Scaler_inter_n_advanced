import sys

def solve(A):
    # Given an array of integers A, find and return the peak element in it. 
    # An array element is peak if it is NOT smaller than its neighbors.

    # For corner elements, we need to consider only one neighbor. We ensure that answer will be unique.

    # NOTE: Users are expected to solve this in O(log(N)) time. The array may have duplicate elements.
    #peak=-sys.maxsize
    
    #Slow approach
    
    # n=len(A)
    # if n ==1:
    #     return A[0]
    
    # if n==0:
    #     return None
    
    
    
    # low=0
    # high=n-1
    # ans=0
    
    # while low<=high:
    #     mid=(low+high)//2
        
    #     if (mid==0 and A[mid+1]<A[mid]) or (mid == (n-1) and A[mid-1]<A[mid]) or (A[mid-1]<A[mid]>A[mid+1]):
    #         return A[mid]
    #     elif A[mid]<A[mid+1]:
    #         low=mid+1
    #     elif A[mid]>A[mid-1]:
    #         ans=A[mid]
    #         high=mid-1
            
    # return ans

    # Slight fast approach
    
    n=len(A)
    if n ==1:
        return A[0]
    
    if n==0:
        return None
    
    if A[1]<=A[0]:
        return A[0]
    if A[n-2]<=A[n-1]:
        return A[n-1]
    
    low=1
    high=n-2
    ans=0
    
    while low<=high:
        mid=(low+high)//2
        
        if A[mid-1]<A[mid] and A[mid]>A[mid+1]:
            return A[mid]
        elif A[mid]<A[mid+1]:
            low=mid+1
        else:            
            high=mid-1
            
    return ans


#print(solve([5, 17, 100, 11]))
#print(solve([1]))
print(solve([ 18, 33, 100, 135, 203, 270, 292, 310, 356, 392, 400, 429, 436, 461, 427, 403, 399, 375, 251, 245, 173, 130, 43 ]))
        
    
    
