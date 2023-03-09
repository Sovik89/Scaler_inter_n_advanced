def checks(n,A,B,M):
    summation=0
    
    
    
    for i in range(M):
        summation+=A[i]
    p1=0
    p2=M-1
    
    if M==n:
        if summation>B:
            return False
    
    for i in range(M,n):
        summation+=A[i]
        summation-=A[p1]
        if summation>B:
            return False
        p1+=1
        
    
    return True

def solve(A,B):
    # Given an array of integers A and an integer B, find 
    # and return the maximum value K such that there is no 
    # subarray in A of size K with the sum of elements greater than B.
    
    n=len(A)
    
    if n==0:
        return 0
    if n==1:
        if A[n]<=B:
            return 1
        else:
            return 0
    low =1#minimum value of non-zero subarrays
    high=len(A)#maximum value of the subarray
    
    ans=0#even if any value of 1 max lenght has summation greater than B
    
    while low<=high:
        mid=(low+high)//2
        if checks(n,A,B,mid):
            ans=mid
            low=mid+1
        else:
            high=mid-1
    
    return ans



#print(solve([5, 17, 100, 11],130))
print(solve([1, 2, 3, 4, 5],10))
        
    