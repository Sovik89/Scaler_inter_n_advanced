def solve(A, B):
    
    n=len(A)
    p1=0
    p2=n-1
    ans=0
    
    while (p1<=n-1 and p2>=0):
        val=A[p1]*A[p2]
        
        if val <B:
            ans+=(p2+1)
            p1+=1
        else:
            p2-=1
    
    return ans%(10**9+7)
    

print(solve([1, 2],5))
        
        
            