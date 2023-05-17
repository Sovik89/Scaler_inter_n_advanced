import sys
sys.setrecursionlimit(10**6)

class Solution:
	# @param A : list of list of integers
	# @return an integer
    def determine_min_path(self,A,i,j,dp):
        if i<0 or j<0:
            return float('inf')
        if i==0 and j==0:
            dp[i][j]=A[i][j]
            return dp[i][j]
        
        if dp[i][j]==-1001:
            dp[i][j]=min(self.determine_min_path(A,i-1,j,dp),self.determine_min_path(A,i,j-1,dp))+A[i][j]
            
        return dp[i][j]

    def minPathSum(self, A):
        n=len(A)
        m=len(A[0])
        if n==1 and m==1:
            return A[0][0]
        dp=[[-1001 for j in range(m)] for i in range(n)]
        
        self.determine_min_path(A,n-1,m-1,dp)
        
        return dp[n-1][m-1]
