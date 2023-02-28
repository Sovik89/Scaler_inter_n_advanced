def solve(A, B):
        
        n=len(A)
        ans=[0]*n
        for b in B:
            L,R,P = b
            
            ans[L-1]+=P
            
            if R<n:
                ans[R]-=P
            #print(A)
        #print(A)
        ans[0] +=A[0]
        for i in range(1,n):
            sum=ans[i-1]+ans[i]+A[i]-A[i-1]
            ans[i]=sum
        
        return ans
    
print(solve([1, 2, 1, 4],[[2, 3, 2],[1, 4, 5],[4, 4, 1]]))