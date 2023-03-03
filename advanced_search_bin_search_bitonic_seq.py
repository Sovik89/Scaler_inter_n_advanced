def solve(A, B):
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
    peak=0
    
    #finding peak or local maxima in the bitonic array
    while low<=high:
        mid=(low+high)//2
        
        if A[mid-1]<A[mid] and A[mid]>A[mid+1]:
            peak=mid
            break
        elif A[mid]<A[mid+1]:
            low=mid+1
        else:            
            high=mid-1
    
    if B==A[peak]:
        return peak
    
    # finding target in 0 to peak-1
    
    low=0
    high=peak-1
    
    while low<=high:
        mid=(low+high)//2
        
        if A[mid]==B:
            return mid
        if A[mid]<B:
            low=mid+1
        if A[mid]>B:            
            high=mid-1
    
    #finding target in peak +1 to n-1
    
    low=peak+1
    high=n-1
    
    while low<=high:
        mid=(low+high)//2
        
        if A[mid]==B:
            return mid
        if A[mid]<B:
            high=mid-1
        if A[mid]>B:
            low=mid+1
    
    return -1


print(solve([5, 6, 7, 8, 9, 10, 3, 2, 1],30))
    
     