import sys
sys.setrecursionlimit(10**6)

def count_squares(dp,i,N):
    if i==0:
        return 0
    
    if dp[i]==(N+1):
        
        for j in range(1,int(i**0.5)+1):
            #taking 1 way and going for i-(j**2) ones
            dp[i]=min(dp[i],count_squares(dp,i-(j**2),N)+1)
            
    return dp[i]

def countMinSquares(A):
    dp=[A+1]*(A+1)
    
    count_squares(dp,A,A)
        
    return dp[A]


print(countMinSquares(12))
    
    
    

