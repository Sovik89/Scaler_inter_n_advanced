import sys
sys.setrecursionlimit(10**6)

class Solution:
	# @param A : list of list of integers
	# @return an integer
    def determinePath(self,matrix,i,j,dp):
        """
        Top down approach
        
        """
        #base condition 1
        if i<0 or j<0:
            return 0
        # determining condition
        if matrix[i][j]==1:
            return 0
        #base condition 2
        if i==0 and j==0:
            return 1
        #dp expression
        if dp[i][j]==-1:
            dp[i][j]=self.determinePath(matrix,i,j-1,dp)+self.determinePath(matrix,i-1,j,dp)

        return dp[i][j]

    def uniquePathsWithObstacles(self, A):
        n=len(A)
        m=len(A[0])
        
        #edge case
        if n==1 and m==1:
            if A[0][0]==1:
                return 0
            else:
                return 1

        dp=[[-1 for j in range(m)] for i in range(n)]
        #print(dp)
        
        self.determinePath(A,n-1,m-1,dp)
        
        #more edge case
        if dp[n-1][m-1]==-1:
            return 0
        return dp[n-1][m-1]