def solve( A):
        N=len(A)
        i=0
        ans=N
        for i in range(N):
            if A[i]!=i+1:
                
                while A[i]!=i+1:
                    ans-=1
                    correct_index=A[i]
                    A[i],A[correct_index-1]=A[correct_index-1],A[i]
                        
        
        return ans