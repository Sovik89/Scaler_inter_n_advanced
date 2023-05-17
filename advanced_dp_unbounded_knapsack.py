import sys
sys.setrecursionlimit(10**6)

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def knapsack(self,i,j,v,w,dp):
        if i==-1 or j==0:
            return 0

        if dp[i][j]==-1:
            z=self.knapsack(i-1,j,v,w,dp)
            if j>=w[i]:
                z=max(z,self.knapsack(i,j-w[i],v,w,dp)+v[i])
            dp[i][j]=z
            
        return dp[i][j]


    def solve(self, A, B, C):
        n=len(B)
        dp=[[-1 for col in range(A+1)] for row in range(n)]

        return self.knapsack(n-1,A,B,C,dp)