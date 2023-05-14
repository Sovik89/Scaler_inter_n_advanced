def solve(A,B,C,D):
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    
    #bottom up approach
    
    n=len(A)
    
    #create array for the values of previous row, each row consists of max values of
    # B*A[i],B*A[i]+C*A[i],B*A[i]+C*A[i]+D*A[i] on each column,
    
    dp =[[float("-inf")]*3]*(n+1)
    
    for i in range(1,n+1):
        
        #for 1st col/B*A[i-1] max value calculation
        
        dp[i][0]=max(dp[i-1][0],B*A[i-1])
        
        # for 2nd col/B*A[i-1]+C*A[i-1] max value calculation
        
        dp[i][1]=max(dp[i-1][1],dp[i][0]+C*A[i-1])
        
        # for 3rd col/B*A[i-1]+C*A[i-1]+D*A[i-1] max value calculation
        
        dp[i][2]=max(dp[i-1][2],dp[i][1]+D*A[i-1])
        
    
    return dp[n][2]
    
    
    #print(dp)
    
    
print(solve([1, 5, -3, 4, -2],2,1,-1))

    
    
    