import sys
sys.setrecursionlimit(10**6)

def adjacent_max_sum(array,i,dp):
    if i==0:
        if dp[0]==0:
            dp[0]=max(array[0][i],array[1][i])
            return dp[0]
    
    elif i==1:
        if dp[1]==0:
            dp[1]=max(adjacent_max_sum(array,i-1,dp),max(array[1][i],array[0][i]))
            return dp[1]
    
    if dp[i]==0:
        dp[i]=max((adjacent_max_sum(array,i-2,dp)+max(array[0][i],array[1][i])),adjacent_max_sum(array,i-1,dp))
        
    return dp[i]

	
def adjacent(A):
    # @param A : list of list of integers
	# @return an integer
    n=len(A[0])
    dp=[0]*n
    
    adjacent_max_sum(A,n-1,dp)
    
    return dp[-1]

print(adjacent([ [1, 2, 3, 4],[2, 3, 4, 5]]))
    