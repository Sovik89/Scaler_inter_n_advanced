def count_steps(dp,A):
    
    if A<=3:
        dp[A]=A
        return dp[A]
    
    
    if dp[A]==0:
        dp[A]=count_steps(dp,A-2)+count_steps(dp,A-1)
        
    return dp[A]
    



def climbStairs(A):
    # @param A : integer
	# @return an integer
    
    dp=[0]*(A+1)
    
    count_steps(dp,A)
    
    
    return dp[A]


print(climbStairs(5))
    
        
    
    
 
     
     
     
     