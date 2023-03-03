def solve(A, B, C):
    """
    Given a sorted array B of integers of size A, 
    and a integer value C, return the ceiling of C which is present in array B.
    """
    
    low = 0
    high = A-1
    ans=-1
    while low<=high:
        mid=(low+high)//2
        
        if B[mid]==C:
            ans=B[mid]
            return B[mid]
        if B[mid]>C:
            ans=B[mid]
            high=mid-1
        if B[mid]<C:
            low=mid+1
            
    return ans

#print(solve(5,[2, 5, 6, 9, 18],7))
print(solve(6,[3, 7, 9, 11, 19, 20],22))  