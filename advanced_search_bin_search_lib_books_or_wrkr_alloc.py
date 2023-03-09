def checks(A,B,n,M):
    pages=0
    student_count=1
    
    for i in range(n):
        if pages+A[i]<=M:
            pages+=A[i]
        else:
            pages=A[i]
            student_count+=1
    
            if student_count>B:
                return False
    return True

def books(A, B):
    n=len(A)
    if n<B:
        return -1
    low=max(A)
    high=sum(A)
    
    ans=-1
    
    while low<=high:
        mid=(low+high)//2
        if checks(A,B,n,mid):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans


print(books([12, 34, 67, 90],2))
            
        
        