def searchRange(A, B):
    """
     Given a sorted array of integers A (0-indexed) of size N, 
     find the starting and the ending position of a given integer B in array A.

     Your algorithm's runtime complexity must be in the order of O(log n).

     Return an array of size 2, such that the first element = starting position of B 
     in A and the second element = ending position of B in A, if B is not found in A 
     return [-1, -1].
    """
    
    ans=[-1,-1]
    n=len(A)
    #leftmost value
    
    low_left=0
    high_left=n-1
    
    while low_left<=high_left:
        mid = (low_left+high_left)//2
        if A[mid]==B:
            ans[0]=mid
            high_left=mid-1
        if A[mid]>B:
            high_left=mid-1
        if A[mid]<B:
            low_left=mid+1
    
    #rightmost value
    
    low_right=0
    high_right=n-1
    
    while low_right<=high_right:
        mid = (low_right+high_right)//2
        if A[mid]==B:
            ans[1]=mid
            low_right=mid+1
        if A[mid]>B:
            high_right=mid-1
        if A[mid]<B:
            low_right=mid+1
    return ans


#print(searchRange([5, 7, 7, 8, 8, 10],8))
print(searchRange([5, 17, 100, 111],3))