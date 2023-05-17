import sys

def minimumTotal(A):
    # @param A : list of list of integers
    # @return an integer
    
    n=len(A)
    j=1
    
    if n==1:
        return A[0][0]
    
    dp=[[0 for col in range(n)] for row in range(n)]# for memoization in nXn scenario
    
    #print(dp)
    
    for k in range(n):
        dp[n-1][k]=A[n-1][k]
    
    i=1
    j=1
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            
            dp[i][j]=min(dp[i+1][j+1],dp[i+1][j])+A[i][j]
        
        
    return dp[0][0]

#print(minimumTotal([[2],[3, 4],[6, 5, 7],[4, 1, 8, 3]]))
#print(minimumTotal([[1]]))
print(minimumTotal([[6,6],[7,8]]))        
        
        
           
    
    
    
    
    